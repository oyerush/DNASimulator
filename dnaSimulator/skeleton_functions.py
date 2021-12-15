from hash_base_functions import *
import numpy as np
# skeleton functions


def get_strand_skeleton(strand):
    # return the skeleton of strand
    skeleton = ""
    last_char = ""
    for x in strand:
        if last_char == x:
            continue
        last_char = x
        skeleton += x
    return skeleton


def get_longest_skeleton(skeletons):
    # find the longest skeleton in list of skeletons
    longest = skeletons[0]
    for skeleton in skeletons:
        if len(longest) < len(skeleton):
            longest = skeleton
    return longest


def get_max_char(char_counter):
    max_char = "A"
    max_counter = 0
    for char, counter in char_counter.items():
        if max_counter < counter and char != "B":
            max_char = char
            max_counter = counter
    return max_char


def get_avarage_skeleton(skeletons):
    flag = 0
    avarage_skeleton = ""
    num_skeletons = len(skeletons)
    pointers = [0]*len(skeletons)
    while flag < num_skeletons:
        char_counter = {"A": 0, "C": 0, "G": 0, "T": 0, "B": 0}
        for i, skeleton in enumerate(skeletons):
            char_counter[skeleton[pointers[i]]] += 1
        next_char = get_max_char(char_counter)
        avarage_skeleton += next_char
        for i, skeleton in enumerate(skeletons):
            if skeleton[pointers[i]] == next_char:
                pointers[i] += 1
                if pointers[i] >= len(skeleton):
                    flag += 1
                    skeletons[i] = "B"
                    pointers[i] = 0
    return avarage_skeleton


def create_cluster_sig(strands, q, ind_dic):
    cluster_sig = np.array([0]*len(ind_dic))
    for strand in strands:
        skeleton = get_strand_skeleton(strand)
        cluster_sig = np.add(cluster_sig, np.array(
            [int(x) for x in bin_sig(skeleton, q, ind_dic)]))
    return cluster_sig.tolist()



def clusters_similarity(sig1, sig2, len1, len2, q):
    similarity = 0
    for x, y in zip(sig1, sig2):
        similarity += abs(y/len2 - x/len1)
    return 1-similarity/(4**q)


def cluster_avarage_homopolymer(strands, avarage_skeleton):
    homopolymer = {}
    homopolymer_avarage = [[x, 0] for x in avarage_skeleton]
    for strand in strands:
        homopolymer[strand] = []
        corrent = ""
        for x in strand:
            if x==corrent:
                homopolymer[strand][-1][1] += 1
            else:
                corrent = x
                homopolymer[strand].append([x,1])
    for strand in strands:
        i=0
        j=0
        while j<len(avarage_skeleton):
            try:
                if homopolymer[strand][i][0] == avarage_skeleton[j]:
                    homopolymer_avarage[j][1] += homopolymer[strand][i][1]
                    i+=1
            except:
                pass
            j+=1
    return [[x[0], x[1]/len(strands)] for x in homopolymer_avarage]


def homopolymer_dist(homopolymer1, homopolymer2, avarages_skeleton):
    i=0
    j=0
    k=0
    homopolymer_dist = 0
    while k<len(avarages_skeleton):
        #print(i, j, k, homopolymer1[i][0], homopolymer2[j][0], avarages_skeleton[k], homopolymer_dist)
        if i<len(homopolymer1) and j<len(homopolymer2) and homopolymer1[i][0] == avarages_skeleton[k] and homopolymer2[j][0] == avarages_skeleton[k]:
            homopolymer_dist += abs(homopolymer1[i][1]-homopolymer2[j][1])
            j+=1
            i+=1
        elif i<len(homopolymer1) and homopolymer1[i][0] == avarages_skeleton[k]:
            homopolymer_dist += homopolymer1[i][1]
            i+=1
        elif j < len(homopolymer2) and homopolymer2[j][0] == avarages_skeleton[k]:
            homopolymer_dist += homopolymer2[j][1]
            j+=1
        k+=1
    while j <len(homopolymer2):
        homopolymer_dist += homopolymer2[j][1]
        j+=1
    while  i < len(homopolymer1):
        homopolymer_dist += homopolymer1[i][1]
        i+=1
    return homopolymer_dist/len(avarages_skeleton)
            


def num_of_chars(strands1, strands2):
    chars = {'A':0, 'C':0, 'G':0, 'T':0}
    avarage_len1 = 0
    avarage_len2 = 0
    for strand in strands1:
        for x in strand:
            chars[x] +=1/len(strands1)
        avarage_len1 += len(strand)
    for strand in strands2:
        for x in strand:
            chars[x] -= 1/len(strands2)
        avarage_len2 += len(strand)
    res = 0
    for x in chars.values():
        res += abs(x)
    return res/((avarage_len1+avarage_len2)/(len(strands2)+len(strands1)))
