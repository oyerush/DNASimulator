import argparse
import os
import shutil
import threading

from simulator import *
import time


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


class StutterCluster:

    def __init__(self, chosen_technology):
        self.technology = chosen_technology
        if platform.system() == "Linux":
            self.shuffled_file = './files/' + self.technology + '/' + 'errors_shuffled.txt'
        elif platform.system() == "Windows":
            self.shuffled_file = 'files/' + self.technology + '/' + 'errors_shuffled.txt'

        if platform.system() == "Linux":
            self.evyat_path = './files/' + self.technology + '/' + 'evyat.txt'
        elif platform.system() == "Windows":
            self.evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'

        self.strands = {}
        self.strands_by_skeleton = {}
        self.skeleton_dist = {}
        self.dist_to_skeleton = {}
        self.cluster = {}

    def get_dict_form_shuffeld(self):
        with open(self.shuffled_file, 'r') as evyat_shuffled:
            for counter, line in enumerate(evyat_shuffled):
                self.strands[counter] = line.rstrip('\n')

    def get_strands_skeleton(self):
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(strand)] = []
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(strand)].append(strand)

    def calculate_dist(self, q):
        anchor = self.get_strands_skeleton().keys()[0]
        anchor_sig = bin_sig(anchor, q)
        for skeleton in self.strands_by_skeleton.keys():
            self.skeleton_dist[skeleton] = ham_dis(anchor_sig, bin_sig(skeleton, q))





    def check(self):
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        for x in self.strands_by_skeleton.keys():
            if len(self.strands_by_skeleton[x]) > 1:
                print(len(self.strands_by_skeleton[x]))
                print(x)
                #print("here:", x)
        return get_strand_skeleton(self.strands[10]), self.strands_by_skeleton[get_strand_skeleton(self.strands[10])]


# checks
cluster = StutterCluster("miseq_twist")
print(cluster.check())