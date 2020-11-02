# Module: error_gen.py

import random
import math
from operator import itemgetter


# special thanks to: https://stackoverflow.com/questions/13221896/python-partial-sum-of-numbers
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i[1]
        yield total


# Generate an error from the error rates dictionary passed as arguments:
# Example of a dictionary:
# {'d': 0.1, 'i': 0.2, 's': 0.1, 'n': 0.6}
def generate_error_type(err_rates: dict) -> str:
    # create a sorted list of the dictionary:
    err_rates_list = []
    for key, value in err_rates.items():
        temp = [key, value]
        err_rates_list.append(temp)
    # sort list in ascending order of values (error rates):
    err_rates_list = sorted(err_rates_list, key=itemgetter(1))
    # draw a random number in the range between 0 and the difference:
    draw = random.uniform(0, 1)
    # f.write('draw: ' + str(draw) + '\n')
    # generate a list of ranges: (0 - x1, x1 - x1+x2, ... , x1+...+xn - xn+1)
    ranges_list = [0]
    ranges_list.extend(list(partial_sums(err_rates_list)))
    # check to which ranges the error belongs:
    for i in range(len(ranges_list) - 1):
        if ranges_list[i] < draw <= ranges_list[i+1]:
            # f.write('range is: ' + str(ranges_list[i]) + ', ' + str(ranges_list[i+1]) + '\n')
            return err_rates_list[i][0]
        if draw == ranges_list[0]:
            return err_rates_list[0][0]


def select_error_location(strand: str):
    strand_len = len(strand)
    # get a random value m that represents the beginning of the strand that gets higher weight:

    m = random.randint(1, math.floor(strand_len/3))
    # randomize an index in the range of [0, len-1]:
    options = ['m', 'rest']
    rates = [0.67, 0.33]
    draw = random.choices(options, weights=rates, k=1)
    loc = 0
    if draw[0] == 'm':
        loc = random.randint(0, m)
    else:
        loc = random.randint(m+1, strand_len-1)
    return loc


"""
Testing:
"""

'''
if __name__ == '__main__':
    
    # error types test:
    
    err_type_f = open('error_types', 'w')
    for j in range(1000):
        result = generate_error_type({'d': 0.1, 'i': 0.2, 's': 0.1, 'n': 0.6})
        result_to_write = str(result) + '\n'
        err_type_f.write(result_to_write)

    err_type_f.close()

    err_type_f = open('error_types', 'r')
    hist = [['d', 0], ['s', 0], ['i', 0], ['n', 0]]
    lines = err_type_f.readlines()
    for line in lines:
        if line == 'd\n':
            hist[0][1] += 1
        if line == 's\n':
            hist[1][1] += 1
        if line == 'i\n':
            hist[2][1] += 1
        if line == 'n\n':
            hist[3][1] += 1
    
    err_type_f.close()

    err_type_ana_f = open('error_types_analysis', 'w')
    err_type_ana_f.write('d appearance rate: ' + str(hist[0][1] / 1000) + '\n')
    err_type_ana_f.write('s appearance rate: ' + str(hist[1][1] / 1000) + '\n')
    err_type_ana_f.write('i appearance rate: ' + str(hist[2][1] / 1000) + '\n')
    err_type_ana_f.write('n appearance rate: ' + str(hist[3][1] / 1000) + '\n')
    
    err_type_ana_f.close()
    

    # error locations test:
    
    error_loc_f = open('error_locations', 'w')

    # http://www.faculty.ucr.edu/~mmaduro/random.htm
    example_strand = "TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCCTA" \
                     "GTGCAATGGGGCTTTTTTTCCATAGTCCTCGAGAGGAGGAGACGTCAGTCCAGATATCTTTGATGTCGTGATTGGAAGGACCCTTGGCCCTCCA" \
                     "CCCTTAGGCAGT"
    example_strand_len = len(example_strand)

    for j in range(1000):
        result = select_error_location(example_strand)
        result_to_write = str(result) + '\n'
        error_loc_f.write(result_to_write)

    error_loc_f.close()

    error_loc_f = open('error_locations', 'r')
    hist = [['1/3 len', 0], ['rest', 0]]
    lines = error_loc_f.readlines()
    for line in lines:
        val = line.rstrip()
        val = int(val)
        if val <= example_strand_len/3:
            hist[0][1] += 1
        else:
            hist[1][1] += 1

    error_loc_f.close()

    err_loc_ana_f = open('error_locations_analysis', 'w')
    err_loc_ana_f.write('1/3 appearance rate: ' + str(hist[0][1] / 1000) + '\n')
    err_loc_ana_f.write('after 1/3 appearance rate: ' + str(hist[1][1] / 1000) + '\n')

    err_loc_ana_f.close()
'''




