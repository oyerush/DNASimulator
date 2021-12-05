import argparse
import os
import shutil
import threading
from stutter_clustering.hash_base_functions import *
from stutter_clustering.skeleton_functions import *
from simulator import *
import time




# check with original functions
def compare_groups(original_cluster, output_cluster):
    # comper the original cluster with the output cluster
    # print num fo correct, false_p, false_n
    correct = 0
    false_p = 0
    corr = []
    f_p = []
    f_n = []
    for x in output_cluster:
        if x in original_cluster:
            corr = x
            correct += 1
        else:
            f_p = x
            false_p += 1
    false_n = len(original_cluster) - correct
    # print("origin:")
    # for x in original_cluster:
    #    print("*", x[:15], "...")
    # print("output:")
    # for x in output_cluster:
    #    print("*", x[:15], "...")
    # for x in original_cluster:
    #    if x not in corr:
    #        f_n += x
    #        break
    return {"correct": correct, "false_p": false_p, "false_n": false_n}
    print("correct:", correct)
    # print("".join(corr))
    print("false_p:", false_p)
    # print("".join(f_n))
    print("false_n:", false_n)
    print("_______")


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
        self.bound = 20
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
        # make strands_by_skeleton - get the skeleton of each strand
        #                           insert the strand to the skeleton element
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(strand)] = []
        for strand in self.strands.values():
            self.strands_by_skeleton[get_strand_skeleton(
                strand)].append(strand)

    def create_group(self, corrent_strands_by_skeleton, q):
        # get the rest of the skeletons (the one that wasn't clustered yet) and size of bin_sig
        # found a group that of all the close skeletons to the longest skeleton
        anchor = get_longest_skeleton(list(corrent_strands_by_skeleton.keys()))
        anchor_sig = bin_sig(anchor, q)
        count = 0
        self.skeleton_dist = {}
        for skeleton in corrent_strands_by_skeleton.keys():
            self.skeleton_dist[skeleton] = ham_dis(
                anchor_sig, bin_sig(skeleton, q))
        group = []
        count = 0
        for skeleton, dis in self.skeleton_dist.items():
            if dis < self.bound:  # 0.3 * len(skeleton):
                group.append(skeleton)
        return get_avarage_skeleton(group.copy()), group

    def get_closest_group(self, avarage_skeleton, q):
        min_dist = len(avarage_skeleton)
        av_skeleton_sig = bin_sig(avarage_skeleton, q)
        min_group = []
        for group_av_skeleton in self.Cluster.keys():
            dist = ham_dis(av_skeleton_sig, bin_sig(group_av_skeleton, q))
            if dist < min_dist:
                min_dist = dist
                min_group = group_av_skeleton
        return min_group

    def get_closest_group_by_sig(self, avarage_skeleton, q):
        min_dist = len(avarage_skeleton)
        av_skeleton_sig = bin_sig(avarage_skeleton, q)
        min_group = []
        for group_av_skeleton in self.Cluster.keys():
            dist = ham_dis(av_skeleton_sig, bin_sig(group_av_skeleton, q))
            if dist < min_dist:
                min_dist = dist
                min_group = group_av_skeleton
        return min_group

    def create_evyat_dict(self):
        in_cluster = 0

        if platform.system() == "Linux":
            evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'
            evyatdict_path = 'files/' + self.technology + '/' + str(
                self.index) + '_evyatdict'
        elif platform.system() == "Windows":
            evyat_path = 'files/' + self.technology + '/' + 'evyat.txt'
            evyatdict_path = 'files/' + self.technology + \
                '/' + str(self.index) + '_evyatdict'
        self.evyat_dict_strings = create_ind(
            self.evyat_dict_strings,  self.index)
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
                    self.evyat_dict_strings[cluster_index].append(
                        line.rstrip('\n'))

    def get_strands_in_group_of_skeleton(self, skeletons):
        strands = []
        for skeleton in skeletons:
            strands += self.strands_by_skeleton[skeleton]
        return strands

    def make_first_level_cluster(self):
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        self.create_evyat_dict()
        self.Cluster = {}
        self.Cluster_info = {}
        count = 0
        f = open("out_txt", "w")
        corrent_strands_by_skeleton = self.strands_by_skeleton.copy()
        while corrent_strands_by_skeleton:
            if count % 50 == 0:
                f.seek(0)
                f.write("\n".join(map(str, self.Cluster_info.values())))
            #count += 1
            avarage_skeleton, group_of_skeleton = self.create_group(
                corrent_strands_by_skeleton, 4)
            # add the new group to the cluster
            if len(group_of_skeleton) > 8:
                self.Cluster[avarage_skeleton] = self.get_strands_in_group_of_skeleton(
                    group_of_skeleton)
                for cluster in self.evyat_dict_strings.values():
                    if self.get_strands_in_group_of_skeleton(
                            group_of_skeleton)[0] in cluster:
                        self.Cluster_info[avarage_skeleton] = compare_groups(
                            cluster, self.Cluster[avarage_skeleton])
            else:
                group_to_add_to = self.get_closest_group(avarage_skeleton, 4)
                self.Cluster[group_to_add_to] += self.get_strands_in_group_of_skeleton(
                    group_of_skeleton)
                for cluster in self.evyat_dict_strings.values():
                    if self.get_strands_in_group_of_skeleton(
                            group_of_skeleton)[0] in cluster:
                        print("befor:", self.Cluster_info[group_to_add_to])
                        self.Cluster_info[group_to_add_to] = compare_groups(
                            cluster, self.Cluster[group_to_add_to])
                        print("after:", self.Cluster_info[group_to_add_to])
            # remove the old group from the cluster
            for skeleton in group_of_skeleton:
                corrent_strands_by_skeleton.pop(skeleton)
        return self.Cluster

    def check(self):
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        print("finish skeleton")
        self.create_evyat_dict()
        print("finish evyat")
        self.Cluster = {}
        corrent_strands_by_skeleton = self.strands_by_skeleton.copy()
        while corrent_strands_by_skeleton:
            anchor, group_of_skeleton = self.create_group(
                corrent_strands_by_skeleton, 4)
            # print(self.strands_by_skeleton[anchor])
            for cluster in self.evyat_dict_strings.values():
                if corrent_strands_by_skeleton[anchor][0] in cluster:
                    print("found anchor cluster")
                    anchors_cluster = cluster
            if len(group_of_skeleton) > 3:
                self.Cluster[anchor] = self.get_strands_in_group_of_skeleton(
                    group_of_skeleton)
                compare_groups(
                    anchors_cluster, self.get_strands_in_group_of_skeleton(group_of_skeleton))
            for skeleton in group_of_skeleton:
                corrent_strands_by_skeleton.pop(skeleton)

        # for x in self.strands_by_skeleton.keys():
        #    if len(self.strands_by_skeleton[x]) > 1:
        #        print(len(self.strands_by_skeleton[x]))
        #        print(x)
                #print("here:", x)
        return get_strand_skeleton(self.strands[10]), self.strands_by_skeleton[get_strand_skeleton(self.strands[10])]


# checks
cluster = StutterCluster("miseq_twist")
cluster.make_first_level_cluster()
