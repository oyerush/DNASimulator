import argparse
import os
import shutil
import threading

from simulator import *
import time



DNA ={
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}

def numberToBase(n, b, size):
    if n == 0:
        return [0]*(size - 1)+[0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return [0]*(size-len(digits[::-1])) + digits[::-1]

def toDNA(x):
    dna_str = ""
    for n in x:
        dna_str += DNA[n]
    return dna_str

def create_ind(m, size):
    for x in [toDNA(numberToBase(x, 4, size)) for x in range(4**size)]:
        m[x] = []
    return m



def ham_dis(x, y):
    # hamming distance between x, y
    dis = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            dis += 1
    return dis


def ind_st(st):
    # convert form DNA-base to decimal-base
    # All 3-grams: AAA,AAG,AAC,AAT,AGA,AGC,...,TTA,TTG,TTC,TTT
    # A-0, G-1, C-2, T-3
    # index of CAT = Decimal representaion of (203)
    N_q = {"A": 0, "C": 1, "G": 2, "T": 3}
    dec = 0
    for i in range(0, len(st)):
        dec += N_q[st[i]] * (4 ** (len(st) - i - 1))
    return dec

def bin_sig(x, q):
    # x - st of DNA
    # q - size of DAN-chunk
    # return binary string
    #   i-th character is 1 if DNAbase(i) in x
    bs = [0] * (4 ** q)
    for i in range(0, len(x) - q + 1):
        st = x[i:i + q]
        bs[ind_st(st)] = 1
    bs_str = ''.join(str(e) for e in bs)
    return bs_str


def get_strand_skeleton(strand):
    skeleton = ""
    last_char = ""
    for x in strand:
        if last_char == x:
            continue
        last_char = x
        skeleton += x
    return skeleton


def get_longest_skeleton(skeletons):
    longest = skeletons[0]
    for skeleton in skeletons:
        if len(longest) < len(skeleton):
            longest = skeleton
    return longest    

    
def compare_groups(original_cluster, output_cluster):
    correct = 0
    false_p = 0
    for x in output_cluster:
        if x in original_cluster:
            correct += 1
        else:
            false_p += 1
    false_n = len(original_cluster) - correct
    print("origin:")
    for x in original_cluster:
        print("*", x[:15], "...")
    print("output:")
    for x in output_cluster:
        print("*", x[:15], "...")
    print("correct:", correct)
    print("false_p:", false_p)
    print("false_n:", false_n)




class StutterCluster:

    def __init__(self, chosen_technology):
        self.technology = chosen_technology
        if platform.system() == "Linux":
            self.shuffled_file = './files/' + self.technology + '/' + 'errors_shuffled.txt'
        elif platform.system() == "Windows":
            self.shuffled_file = 'files/' + self.technology + '/' + 'errors_shuffled.txt'

        if platform.system() == "Linux":
            self.evyat_path = './/files/' + self.technology + '/' + 'evyat.txt'
        elif platform.system() == "Windows":
            self.evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'
        self.index = 4
        self.strands = {}
        self.strands_by_skeleton = {}
        self.skeleton_dist = {}
        self.dist_to_skeleton = {}
        self.cluster = {}
        self.evyat_dict_strings = {}

    def get_dict_form_shuffeld(self):
        with open(self.shuffled_file, 'r') as evyat_shuffled:
            for counter, line in enumerate(evyat_shuffled):
                self.strands[counter] = line.rstrip('\n')

    def get_strands_skeleton(self):
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(strand)] = []
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(strand)].append(strand)

    def create_group(self, q):
        anchor = get_longest_skeleton(list(self.strands_by_skeleton.keys()))
        anchor_sig = bin_sig(anchor, q)
        count = 0
        for skeleton in self.strands_by_skeleton.keys():
            self.skeleton_dist[skeleton] = ham_dis(anchor_sig, bin_sig(skeleton, q))
        group = []
        count = 0
        for skeleton, dis in self.skeleton_dist.items(): 
            if dis < 20: #0.3 * len(skeleton):
                group.append(skeleton)
        return anchor, group





    def create_evyat_dict(self):
        in_cluster = 0

        if platform.system() == "Linux":
            evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'
            evyatdict_path = 'files/' + self.technology + '/' + str(
                self.index) + '_evyatdict'
        elif platform.system() == "Windows":
            evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'
            evyatdict_path = 'files/' + self.technology + '/' + str(self.index) + '_evyatdict'
        self.evyat_dict_strings = create_ind(self.evyat_dict_strings,  self.index)
        print("start evyat")
        with open(evyat_path, 'r') as evyatfile:
            for line in evyatfile:
                if line.strip() != '' and '*' not in line.strip() and in_cluster == 0:
                    in_cluster = 1
                    cluster_index = line[:self.index]
                    continue
                if line.strip() == '':
                    in_cluster = 0
                    continue
                if '*' in line.strip():
                    continue
                if line.strip() != '' and '*' not in line.strip() and in_cluster == 1:
                    self.evyat_dict_strings[cluster_index].append(line.rstrip('\n'))

    def get_strands_in_group_of_skeleton(self, skeletons):
        strands = []
        for skeleton in skeletons:
            strands += self.strands_by_skeleton[skeleton]
        return strands

    def check(self):
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        print("finish skeleton")
        self.create_evyat_dict()
        print("finish evyat")
        anchor, group_of_skeleton = self.create_group(4)
        print(self.strands_by_skeleton[anchor])
        for cluster in self.evyat_dict_strings.values():
            if self.strands_by_skeleton[anchor][0] in cluster:
                print("found anchor cluster")
                anchors_cluster = cluster
        
        compare_groups(anchors_cluster, self.get_strands_in_group_of_skeleton(group_of_skeleton))
        
        
        #for x in self.strands_by_skeleton.keys():
        #    if len(self.strands_by_skeleton[x]) > 1:
        #        print(len(self.strands_by_skeleton[x]))
        #        print(x)
                #print("here:", x)
        return get_strand_skeleton(self.strands[10]), self.strands_by_skeleton[get_strand_skeleton(self.strands[10])]
        
        
# checks
cluster = StutterCluster("miseq_twist")
cluster.check()