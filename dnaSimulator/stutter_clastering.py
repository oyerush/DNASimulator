import argparse
import os
import shutil
import threading
# from stutter_clustering.hash_base_functions import *
from skeleton_functions import *
from simulator import *
import time
from cluster_comper import *
from threading import Thread
import time
from matplotlib import pyplot as plt
import random
import pickle
from datetime import datetime
from leven import levenshtein
from index_dic_generator import *
from scipy.spatial.distance import hamming

# check with original functions
def compare_groups(original_cluster, output_cluster):
    # comper the original cluster with the output cluster
    # print num fo correct, false_p, false_n
    correct = 0
    false_p = 0
    for x in output_cluster:
        if x in original_cluster:
            correct += 1
        else:
            false_p += 1
    false_n = len(original_cluster) - correct
    return {"correct": correct, "false_p": false_p, "false_n": false_n}


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
        self.bound = 35
        self.strands = {}
        self.strands_by_skeleton = {}
        self.skeletons_sig = {}
        self.skeleton_dist = {}
        self.dist_to_skeleton = {}
        self.cluster = {}
        self.evyat_dict_strings = {}
        self.small_groups = []
        self.Cluster = {}
        self.l = 0
        self.union_count = 0
        self.cluster_compare = None
        self.clean_ran = True
        self.index_gen = generate_indx_dic(4)


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

    def get_skeletons_sig(self, q):
        self.l = len(get_longest_skeleton(self.strands_by_skeleton.keys()))
        for skeleton in self.strands_by_skeleton.keys():
            self.skeletons_sig[skeleton] = bin_sig(skeleton, q, self.index_gen.get_ind_dic(), self.l)

    def create_group(self, current_strands_by_skeleton, q, anchor=""):
        # get the rest of the skeletons (the one that wasn't clustered yet) and size of bin_sig
        # found a group that of all the close skeletons to the longest skeleton
        if anchor == "":
            anchor = get_longest_skeleton(list(current_strands_by_skeleton.keys()))
            # anchor = get_strand_skeleton(random.choice(list(current_strands_by_skeleton.keys())))
        first_group = {}
        group = []
        group_strands = []
        for skeleton in current_strands_by_skeleton.keys():
            dist = levenshtein(skeleton[:50], anchor[:50])
            if dist <= 20:
                first_group[skeleton] = dist

        # Alternative for rough clustering: rough cluster only a specific cluster
        # all the strands from the specific skeleton are here, but also a few others
        anchor_sig = self.skeletons_sig[anchor]
        for skeleton, dist in first_group.items():
            if ham_dis(anchor_sig, self.skeletons_sig[skeleton]) < max(60, -4*dist+140):#max(60, -3.5*dist+83):
                group.append(skeleton)
                group_strands += current_strands_by_skeleton[skeleton]

        return ",".join([str(x) for x in create_cluster_sig(group_strands, 4, self.index_gen.get_ind_dic(), self.l)]), group

    def get_closest_group(self, average_skeleton, q):
        min_dist = len(average_skeleton)
        av_skeleton_sig = bin_sig(average_skeleton, q, self.index_gen.get_ind_dic())
        min_group = []
        for group_av_skeleton in self.Cluster.keys():
            dist = ham_dis(av_skeleton_sig, bin_sig(group_av_skeleton, q, self.index_gen.get_ind_dic()))
            if dist < min_dist:
                min_dist = dist
                min_group = group_av_skeleton
        return min_group

    def get_closest_group_by_sig(self, new_cluster_sig, new_len, q):
        # get the sig of the new cluster and his len
        # return [], false if one of the elements aren't correct
        # return [], True if the size of the new group is smaller than 3 and max similarity is high but not enough
        # return max similarity group if found one and the True of false refer to if the cluster should not be merged
        max_similarity = 0
        new_cluster_sig_arr = [int(x) for x in new_cluster_sig.split(",")]
        max_similarity_group = ""
        max_stands_len = 0
        for cluster_sig, strands in self.Cluster.items():
            if new_len == 0 or len(strands) == 0:
                return [], False
            new_similarity = clusters_similarity(
                new_cluster_sig_arr, [int(x) for x in cluster_sig.split(",")], new_len, len(strands), q)
            if max_similarity < new_similarity:
                max_similarity = new_similarity
                max_similarity_group = cluster_sig
                max_stands_len = len(strands)
        min_len = min(new_len, max_stands_len)
        #if new_len < 5:
        #    print(" -", max_similarity)
        #else:
        #    print(max_similarity)
        if max_similarity < 0.8:#min(0.003 * min_len + 0.902, 0.94):
            if max_similarity > 0.887 and new_len <= 3:
                return [], True
            return max_similarity_group, False
        return max_similarity_group, True

    def create_evyat_dict(self):
        in_cluster = 0
        print("start evyat")
        count = 0
        with open(self.evyat_path, 'r') as evyatfile:
            for line in evyatfile:
                if line.strip() != '' and '*' not in line.strip() and in_cluster == 0:
                    in_cluster = 1
                    cluster_index = count
                    self.evyat_dict_strings[cluster_index] = []
                    count += 1
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
            try:
                strands += self.strands_by_skeleton[skeleton]
            except:
                pass
        return strands

    def make_first_level_cluster(self):
        total_start = time.time()
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        self.create_evyat_dict()
        self.get_skeletons_sig(4)
        self.cluster_compare = ClusterComper(self.evyat_dict_strings.values())
        self.cluster_compare.loading_bar(0)
        if not self.clean_ran:
            Thread(target=self.cluster_compare.app, args=()).start()
        last_present = 0
        f = open("temp.txt", "w")
        current_strands_by_skeleton = self.strands_by_skeleton.copy()
        while current_strands_by_skeleton:
            cluster_sig, group_of_skeleton = self.create_group(
                current_strands_by_skeleton, 4)
            group_to_add_to, is_part = self.get_closest_group_by_sig(cluster_sig,
                                                                     len(self.get_strands_in_group_of_skeleton(
                                                                         group_of_skeleton)), 4)
            # add the new group to the cluster
            if not is_part:  # len(group_of_skeleton) > 8:
                self.Cluster[cluster_sig] = self.get_strands_in_group_of_skeleton(
                    group_of_skeleton)

            elif group_to_add_to:
                self.Cluster[group_to_add_to] += self.get_strands_in_group_of_skeleton(
                    group_of_skeleton)
                tmp_cluster = self.Cluster.pop(group_to_add_to)
                self.Cluster[",".join(
                    [str(x) for x in create_cluster_sig(tmp_cluster, 4, self.index_gen.get_ind_dic(), self.l)])] = tmp_cluster
                self.union_count += 1
            self.cluster_compare.update_state(self.Cluster.values())
            for skeleton in group_of_skeleton:
                current_strands_by_skeleton.pop(skeleton)
            presents = 100 * (len(self.strands_by_skeleton) - len(current_strands_by_skeleton)) / len(
                self.strands_by_skeleton)
            if presents - int(last_present) >= 1:
                last_present = presents
                self.cluster_compare.loading_bar(presents)
        print("total time:", time.time() - total_start,
              "union count:", self.union_count)
        self.cluster_compare.update_state(self.Cluster.values())
        self.cluster_compare.final_check()
        return self.Cluster

    def make_second_level_clustering(self):
        start_2 = time.time()
        counter = 0
        last_present = 0
        self.cluster_compare.loading_bar(0)
        for group in self.small_groups:
            current_strands_by_skeleton = self.strands_by_skeleton
            if len(self.create_group(current_strands_by_skeleton, 4, group[0])) <= len(group):
                self.Cluster[",".join(
                    [str(x) for x in create_cluster_sig(group, 4, self.index_gen.get_ind_dic(), self.l)])] = self.get_strands_in_group_of_skeleton(group)
            counter += 1
            presents = 100*counter/len(self.small_groups)
            if presents - int(last_present) >= 1:
                last_present = presents
                self.cluster_compare.loading_bar(presents)
        print("total time:", time.time() - start_2)
        return self.Cluster

    def plot(self, l):
        self.get_dict_form_shuffeld()
        self.get_strands_skeleton()
        self.create_evyat_dict()
        self.l = len(get_longest_skeleton(self.strands_by_skeleton.keys()))
        for strands in self.evyat_dict_strings.values():
            if len(strands) == 1:
                anchor = get_strand_skeleton(strands[0])
        #anchor = get_strand_skeleton(self.evyat_dict_strings[0][0])
        #anchor = get_longest_skeleton(list(self.strands_by_skeleton.keys()))
        anchor = get_strand_skeleton(random.choice(list(self.strands.values())))
        X = []
        Y = []
        cluster = []
        C = []
        D = []
        for strands in self.evyat_dict_strings.values():
            if self.strands_by_skeleton[anchor][0] in strands:
                cluster = strands
            # i += 1
        print(len(anchor))
        print(len(cluster))
        anchor_sig = bin_sig(anchor, 4, self.index_gen.get_ind_dic(), self.l)
        k = random.choice(list(range(len(self.evyat_dict_strings.values()))))
        s = time.time()
        for i, strands in enumerate(self.evyat_dict_strings.values()):
            #if len(strands) == 1:
                #k = i
            skeletons = [get_strand_skeleton(x) for x in strands]
            X.append([])
            Y.append([])
            if strands == cluster:
                continue

            # print(len(skeletons))
            for skeleton in skeletons:
                if i == k:
                    C.append(levenshtein(skeleton[:l], anchor[:l]))
                    # for skeleton in corrent_strands_by_skeleton.keys():
                    D.append(ham_dis(
                        anchor_sig, bin_sig(skeleton, 4, self.index_gen.get_ind_dic(), self.l)))
                X[i].append(levenshtein(skeleton[:l], anchor[:l]))
                # for skeleton in corrent_strands_by_skeleton.keys():
                Y[i].append(ham_dis(
                    anchor_sig, bin_sig(skeleton, 4, self.index_gen.get_ind_dic(), self.l)))
                # Y[i].append(len(skeleton)*10)
        # print(X)
        colors = "bgrcmykw"
        print("time:", time.time() - s)
        i = 0
        for x, y in zip(X, Y):
            plt.scatter(x, y, c="b")
            i += 1
        A = [0]
        B = [0]
        skeletons = [get_strand_skeleton(x) for x in cluster]
        for skeleton in skeletons:
            A.append(levenshtein(skeleton[:l], anchor[:l]))
            B.append(ham_dis(
                anchor_sig, bin_sig(skeleton, 4, self.index_gen.get_ind_dic(), self.l)))
        plt.scatter(A, B, c="r")
        plt.scatter(C, D, c="g")
        plt.show()


def write_clusters_to_file(Clusters, group_type="cluster"):
    date = datetime.now()
    with open(group_type + '_' + date.strftime('%d_%m-%H_%M') + '.out', 'wb') as f:
        print(len(Clusters))
        pickle.dump(Clusters, f)


def get_clusters_from_file(filename):
    with open(filename, 'r') as f:
        return pickle.load(f)


cluster = StutterCluster("miseq_twist")
# cluster.plot(50)
write_clusters_to_file(cluster.make_first_level_cluster())
#write_clusters_to_file(cluster.make_second_level_clustering(), "final_cluster")
#cluster.cluster_compare.update_state(cluster.Cluster.values())
#cluster.cluster_compare.final_check()