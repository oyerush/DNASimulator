from sklearn import metrics
from sklearn.cluster import DBSCAN

import pandas as pd
import numpy as np

from leven import levenshtein

import os

import warnings
warnings.filterwarnings('ignore')


def create_real_labels(evyat_path):
    counter = -1
    mini_counter = 0
    with open('input/evyat_with_labels.txt', 'w') as evyat_labels:
        evyat_labels.truncate(0)
        evyat_labels.write('label\n')
    with open(evyat_path, 'r') as input_f:
        with open('input/evyat_with_labels.txt', 'a') as evyat_labels:
            with open('input/errors_shuffled_clusters.txt', 'w') as evyat_shuffled:
                for line in input_f:
                    if '*' in line.strip():
                        counter = counter + 1
                        # evyat_labels.write(str(counter) + line)
                        # evyat_labels.write(str(counter) + '\n')
                        mini_counter = 0
                    if line.strip() == '':
                        mini_counter = mini_counter + 1
                        continue
                    if counter > -1 and line.strip() != '' and '*' not in line.strip() and mini_counter < 2:
                        # evyat_labels.write(str(counter) + line)
                        evyat_labels.write(str(counter) + '\n')
                        evyat_shuffled.write(line)
    dataframe1 = pd.read_csv('input/evyat_with_labels.txt')
    dataframe1.to_csv('input/real_labels.csv', index=None)
    os.remove('input/evyat_with_labels.txt')
    print(counter)


def demo_dbscan_levenshtein_from_file(evyat_path, eps, min_samples):
    import linecache

    create_real_labels(evyat_path)

    def lev_metric(x, y):
        i, j = int(x[0]), int(y[0])  # extract indices
        line_i = linecache.getline('input/errors_shuffled_clusters.txt', i+1)
        line_j = linecache.getline('input/errors_shuffled_clusters.txt', j+1)
        return levenshtein(line_i, line_j)

    data_len = sum(1 for i in open('input/errors_shuffled_clusters.txt', 'rb'))
    X = np.arange(data_len).reshape(-1, 1)
    # result = dbscan(X, metric=lev_metric, eps=3, min_samples=3, algorithm='brute')
    # try eps = 4 and min_samples = 3
    result2 = DBSCAN(metric=lev_metric, eps=eps, min_samples=min_samples, algorithm='brute').fit(X)
    # pd.DataFrame(result[1]).to_csv("output/dbscan_labels_5x5clusters.csv")
    pd.DataFrame(result2.labels_).to_csv('output/dbscan_labels.csv')

    labels_csv = pd.read_csv('input/real_labels.csv', skiprows=1, names=['label'])
    labels = labels_csv['label']

    print("Homogeneity score: ", metrics.homogeneity_score(labels, result2.labels_))
    print("Completeness score ", metrics.completeness_score(labels, result2.labels_))
    print("V measure score ", metrics.v_measure_score(labels, result2.labels_))
    print("Adjusted rand score: ", metrics.adjusted_rand_score(labels, result2.labels_))
    print("Adjusted mutual info scores: ", metrics.adjusted_mutual_info_score(labels, result2.labels_))
    print("Silhouette score: ", metrics.silhouette_score(X, result2.labels_))

    print('done')


def dbscan_fixed_metric(num_of_strands):
    import linecache

    def lev_metric(x, y):
        i, j = int(x[0]), int(y[0])  # extract indices
        line_i = linecache.getline('input/errors_shuffled_100clusters.txt', i+1)
        line_j = linecache.getline('input/errors_shuffled_100clusters.txt', j+1)
        index_lev = levenshtein(line_i[25:45], line_j[25:45])

        # 10 clusters
        # result = dbscan(X, metric=lev_metric, eps=2, min_samples=20, algorithm='brute')
        # 20 clusters
        # result = dbscan(X, metric=lev_metric, eps=2, min_samples=30, algorithm='brute')

        # trial 1
        # if index_lev <= 1:
        #     return index_lev
        # return levenshtein(line_i, line_j)

        # trial 2 (much faster, and seems good)
        # print(str(i) + ' , ' + str(j))
        # if index_lev > 1:
        #     return 500
        # else:
        #     return levenshtein(line_i, line_j)

        # trial 3
        # if i % 200 == 0:
        #     print(str(i) + ' , ' + str(j))
        if index_lev > 3:
            return 500
        else:
            return levenshtein(line_i, line_j)

    data_len = sum(1 for i in open('input/errors_shuffled_' + num_of_strands + 'clusters.txt', 'rb'))
    X = np.arange(data_len).reshape(-1, 1)
    result2 = DBSCAN(metric=lev_metric, eps=3, min_samples=30, algorithm='brute').fit(X)
    # result2 = DBSCAN(metric=lev_metric, eps=4, min_samples=3, algorithm='brute').fit(X)
    pd.DataFrame(result2.labels_).to_csv('output/fixed_dbscan_labels_' + num_of_strands + 'clusters.csv')

    labels_csv = pd.read_csv('input/real_labels_' + num_of_strands + '.csv', skiprows=1, names=['label'])
    labels = labels_csv['label']

    print("Homogeneity score: ", metrics.homogeneity_score(labels, result2.labels_))
    print("Completeness score ", metrics.completeness_score(labels, result2.labels_))
    print("V measure score ", metrics.v_measure_score(labels, result2.labels_))
    print("Adjusted rand score: ", metrics.adjusted_rand_score(labels, result2.labels_))
    print("Adjusted mutual info scores: ", metrics.adjusted_mutual_info_score(labels, result2.labels_))
    print("Silhouette score: ", metrics.silhouette_score(X, result2.labels_))

    print('done')