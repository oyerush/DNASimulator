from skeleton_functions import *
from hash_base_functions import *
import sys, os

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
    return correct, false_p, false_n


class ClusterComper:

    def __init__(self, correct_clusters):
        self.correct_clusters = list(correct_clusters)
        self.coorent_clusters = []
        with open("cluster_comper2.txt", "w") as f:
            f.write("")


    def update_state(self, coorent_clusters):
        self.coorent_clusters = list(coorent_clusters)
    

    def print_stat(self):
        #stat = {}
        with open("cluster_comper2.txt", "a") as f:
            f.write("____________new____________\n")
            coorent_num_of_strands = len([x for x in self.coorent_clusters])
            correct_num_of_strands = 0
            for i, cluster in enumerate(self.correct_clusters):
                #stat[cluster] = []
                
                correct_num_of_strands += len(cluster)
                f.write(str(i) + " n: " + str(len(cluster)))
                for j, group in enumerate(self.coorent_clusters):
                    for strand in cluster:
                        if strand in group:
                            c, p, n = compare_groups(cluster, group)
                            f.write("{id: " + str(j) + ", c: " + str(c) + ", p: "+ str(p) + " n: " + str(n)+"}")
                            #stat[cluster].append({"id": j, "c": c, "p": p, "n": n})
                            break
                f.write("\n")
            f.write(str(coorent_num_of_strands) + " out of: " + str(correct_num_of_strands))
                        

    def app(self):
        inp = ""
        while inp != "e":
            inp = input("r - refresh and print\ns <id1> <id2> - print similarity\nh <id1> <id2> - print homopolymer dist\nc <id1> <id2> - print char dist\ne - exit:")
            try:
                if inp[0] == "r":
                    self.print_stat()
                elif inp[0] == "s":
                    #print(self.coorent_clusters[0])
                    group1 = self.coorent_clusters[int(inp.split(" ")[1])]
                    group2 = self.coorent_clusters[int(inp.split(" ")[2])]
                    sig1 = create_cluster_sig(group1, 4)
                    sig2 = create_cluster_sig(group2, 4)
                    print("dist:", clusters_similarity(sig1, sig2, len(group1), len(group2), 4))
                elif inp[0] == "h":
                    group1 = self.coorent_clusters[int(inp.split(" ")[1])]
                    group2 = self.coorent_clusters[int(inp.split(" ")[2])]
                    skeletons1 = [get_strand_skeleton(x) for x in group1]
                    skeletons2 = [get_strand_skeleton(x) for x in group2]
                    avg_skeleton1 = get_avarage_skeleton(skeletons1)
                    avg_skeleton2 = get_avarage_skeleton(skeletons2)
                    homopolymer1 = cluster_avarage_homopolymer(group1, avg_skeleton1)
                    homopolymer2 = cluster_avarage_homopolymer(group2, avg_skeleton2)
                    avg_skeletons = get_avarage_skeleton(
                        [avg_skeleton1, avg_skeleton2])
                    print("dist:", homopolymer_dist(homopolymer1, homopolymer2, avg_skeletons))
                elif inp[0] == "":
                    group1 = self.coorent_clusters[int(inp.split(" ")[1])]
                    group2 = self.coorent_clusters[int(inp.split(" ")[2])]
                    print("dist:", num_of_chars())
            except:
                print("error")



            