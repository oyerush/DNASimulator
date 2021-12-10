import time

from skeleton_functions import *
from hash_base_functions import *
import sys, os
from progress.bar import Bar
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
        self.correct_len = 0
        self.outfile = "cluster_comper4.txt"
        for x in self.correct_clusters:
            self.correct_len += len(x)
        self.coorent_clusters = []
        self.first_time = time.time()
        with open(self.outfile, "w") as f:
            f.write("")


    def update_state(self, coorent_clusters):
        self.coorent_clusters = list(coorent_clusters)
    

    def print_stat(self):
        #stat = {}
        with open(self.outfile, "a") as f:
            f.write("____________new____________\n")
            coorent_num_of_strands = 0
            for x in self.coorent_clusters:
                coorent_num_of_strands += len(x)
            for i, cluster in enumerate(self.correct_clusters):
                #stat[cluster] = []
                
                f.write(str(i) + " n: " + str(len(cluster)))
                for j, group in enumerate(self.coorent_clusters):
                    for strand in cluster:
                        if strand in group:
                            c, p, n = compare_groups(cluster, group)
                            f.write("{id: " + str(j) + ", c: " + str(c) + ", p: "+ str(p) + " n: " + str(n)+"}")
                            #stat[cluster].append({"id": j, "c": c, "p": p, "n": n})
                            break
                f.write("\n")
            f.write(str(coorent_num_of_strands) + " out of: " + str(self.correct_len))
                        
    def loading_bar(self, presents):
        print("\r["+"#"*int(presents)+" "*(100-int(presents))+"] %"+str(presents)[:5] + " total sec: "+str(time.time()-self.first_time)[:10], end="")

    def final_check(self):
        self.print_stat()
        with open(self.outfile, "r") as f:
            clusters = {}
            total_correct = 0
            total_false_p = 0
            total_false_c = 0
            total_c = 0
            total_p = 0
            total_n = 0
            for i in range(4190):
                clusters[i] = {"c": 0, "p": 0, "n": 0}
            count = 0
            for line in f.readlines():
                try:
                    line_clusters = line.split("{")[1:]
                    num_of_strends = int(line.split("n: ")[1].split("{")[0])
                    _corrent_n = num_of_strends
                    _max_c = 0
                    _corrent_p = 0
                    for cluster in line_clusters:
                        id = int(cluster.split("id: ")[1].split(",")[0])
                        c = int(cluster.split("c: ")[1].split(",")[0])
                        p = int(cluster.split("p: ")[1].split(" ")[0])
                        n = int(cluster.split("n: ")[1].split("}")[0])

                        if clusters[id]["c"] < c:
                            total_correct -= clusters[id]["c"]
                            total_false_p -= clusters[id]["p"]
                            # total_false_c -= clusters[id]["n"]
                            total_correct += c
                            total_false_p += p
                            # total_false_c += n
                            clusters[id] = {"c": c, "p": p, "n": n}
                        if _max_c < c:
                            _corrent_n = n
                            _max_c = c
                            _corrent_p = p
                    total_p += _corrent_p
                    total_n += _corrent_n
                    total_c += _max_c
                    print(count, "\%correct:", 100 * _max_c / num_of_strends,
                          "\%contamination:", 100 * _corrent_p / _max_c)
                    count += 1
                except:
                    pass

            num_of_strends = total_correct + total_false_p
            print("number of strands:", total_correct + total_false_p)
            print("number of clusters:", count)
            print("total_c", total_c)
            print("total_p", total_p)
            print("total_n", total_n)
            print(count, "\%correct:", 100 * total_c / num_of_strends)
            print(count, "\%contamination:", 100 * total_p / total_c)

    def app(self):
        inp = ""
        while inp != "e":
            inp = input("r - refresh and print\ns <id1> <id2> - print similarity\nh <id1> <id2> - print homopolymer dist\nc <id1> <id2> - print char dist\ne - exit:\n")
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
                    pass
                    #group1 = self.coorent_clusters[int(inp.split(" ")[1])]
                    #group2 = self.coorent_clusters[int(inp.split(" ")[2])]
                    #print("dist:", num_of_chars())
            except:
                print("error")
