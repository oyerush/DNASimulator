# Module: error_gen.py

import random
import math
from operator import itemgetter


'''
How to use:

1. generate_error_type
2. select_error_location
3. inject error


Strings of types of errors supported (in dictionary):

'd'     - deletion (one base)
'ld'    - long deletion (multiple base deletion)
'i'     - insertion
's'     - substitution
'n'     - none (no error)

'''


# special thanks to: https://stackoverflow.com/questions/13221896/python-partial-sum-of-numbers
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i[1]
        yield total


# Error Simulation class.
# Holds the attributes needed for error simulation:
# @ error_rates - dictionary of the error rates used in the simulation.
#       Example of a dictionary:
#       {'d': 0.1, 'i': 0.2, 's': 0.1, 'n': 0.6}
# @ err_type - the error type to use in modifications.
#       Initialized to None. Use generate_error_type to generate a valid error type.
# @ err_rate - the error rate to use in modifications.
#       Initialized to 0. Use generate_error_type to get a valid error rate.
class ErrorSimulation:
    def __init__(self, error_rates):
        self.error_rates = error_rates
        self.err_type = None
        self.err_rate = 0
        self.synthesis_method = None
        self.sequencing_method = None

    # Generate an error from the error rates dictionary passed as arguments:
    # Saves the generated type in the class variable err_type.
    # Saves the generated error's rate in the class variable err_rate.
    def generate_error_type(self):
        # create a sorted list of the dictionary:
        err_rates_list = []
        for key, value in self.error_rates.items():
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
                self.err_type = err_rates_list[i][0]
                self.err_rate = err_rates_list[i][1]
            if draw == ranges_list[0]:
                self.err_type = err_rates_list[0][0]
                self.err_rate = err_rates_list[i][1]

    # Generates a location for the error injection in the range of the given strand's length, giving a higher priority
    # to the beginning 1/3 of the strand.
    # Params:
    # @ strand - the strand to generate the error location of.
    # Return:
    # $ index - the index of the error location.
    @staticmethod
    def select_error_location(strand: str) -> int:
        strand_len = len(strand)
        # get a random value m that represents the beginning of the strand that gets higher weight:
        m = random.randint(0, math.floor(strand_len/3))
        # randomize an index in the range of [0, len-1] giving a higher ratio to the part before m:
        options = ['m', 'rest']
        rates = [0.67, 0.33]  # 2:1 ratio!
        draw = random.choices(options, weights=rates, k=1)
        index = 0
        if draw[0] == 'm':
            index = random.randint(0, m)
        else:
            index = random.randint(m+1, strand_len-1)
        return index

    # Inject deletion to the given strand, starting from the base in `index` location of the strand.
    # Returns a strand with the injected error.
    def inject_deletion(self, strand: str, index: int) -> str:
        modified_strand = ""
        if self.err_type == 'd':
            # single base deletion:
            if index == len(strand)-1:
                modified_strand = strand[:index]
            else:
                modified_strand = strand[:index] + strand[index + 1:]
        elif self.err_type == 'ld':
            # multiple base deletion:
            # https://www.biorxiv.org/content/biorxiv/early/2019/11/13/840231/F15.large.jpg?width=800&height=600&carousel=1
            # https://www.biorxiv.org/content/biorxiv/early/2019/11/13/840231/F12.large.jpg?width=800&height=600&carousel=1
            options = [2, 3, 4, 5, 6]
            rates = [2.8 * (10 ** (-4)),
                     7.75 * (10 ** (-5)),
                     3.25 * (10 ** (-5)),
                     10 ** (-6),
                     5.5 * (10 ** (-8))]
            draw = random.choices(options, weights=rates, k=1)
            deletion_length = draw[0]
            if index + deletion_length > len(strand) - 1:
                modified_strand = strand[:index]
            else:
                modified_strand = strand[:index] + strand[index + deletion_length:]
        return modified_strand

    # Inject insertion to the given strand, starting from the base in `index` location of the strand.
    # Returns a strand with the injected error.
    def inject_insertion(self, strand: str, index: int):
        # TODO: check rates according to pre-insertion base?
        options = ['A', 'T', 'G', 'C']
        rates = [1, 1, 1, 1]
        draw = random.choices(options, weights=rates, k=1)
        modified_strand = strand[:index] + draw[0] + strand[index:]
        return modified_strand

    # Inject substitution to the given strand, starting from the base in `index` location of the strand.
    # Returns a strand with the injected error.
    def inject_substitution(self, strand: str, index: int):
        modified_strand = list(strand)
        # TODO: check rates according to base:
        bases = ['A', 'T', 'G', 'C']
        options = []
        for b in bases:
            if b != modified_strand[index]:
                options.append(b)
        # Note: 'options' is defined by 'bases' so the order is always the same as in 'bases'.
        # Set rates according to the base:
        rates = [1, 1, 1]
        # if modified_strand[index] == 'G':
        #     rates = []
        draw = random.choices(options, weights=rates, k=1)
        modified_strand[index] = draw[0]
        ''.join(modified_strand)
        return modified_strand

    # Inject the error type to the given strand, starting from the base in `index` location of the strand.
    # Returns a strand with the injected error.
    def inject_error(self, strand: str, error_type: str, index: int):
        # check error type and act accordingly:
        if error_type == 'd' or error_type == 'ld':
            return self.inject_deletion(strand, index)
        elif error_type == 'i':
            return self.inject_insertion(strand, index)
        elif error_type == 's':
            return self.inject_substitution(strand, index)
        else:
            return strand  # do nothing if no error is intended


"""
Testing:
"""


if __name__ == '__main__':
    
    # error types test:

    simulator = ErrorSimulation({'d': 9.58 * (10 ** (-4)),
                                 'ld': 2.33 * (10 ** (-4)),
                                 'i': 5.81 * (10 ** (-4)),
                                 's': 1.32 * (10 ** (-3)),
                                 'n': 0.996908})
    
    err_type_f = open('error_types', 'w')
    for j in range(1000):
        simulator.generate_error_type()
        result_to_write = str(simulator.err_type) + '\n'
        err_type_f.write(result_to_write)

    err_type_f.close()

    err_type_f = open('error_types', 'r')
    hist = [['d', 0], ['ld', 0], ['s', 0], ['i', 0], ['n', 0]]
    lines = err_type_f.readlines()
    for line in lines:
        if line == 'd\n':
            hist[0][1] += 1
        if line == 'ld\n':
            hist[1][1] += 1
        if line == 's\n':
            hist[2][1] += 1
        if line == 'i\n':
            hist[3][1] += 1
        if line == 'n\n':
            hist[4][1] += 1
    
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
        result = simulator.select_error_location(example_strand)
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

    # deletion test:

    del_loc = simulator.select_error_location(example_strand)

    simulator.err_type = 'd'
    new_strand = simulator.inject_deletion(example_strand, del_loc)
    deletion_f = open('deletion', 'w')
    deletion_f.write('single base:\n')
    deletion_f.write('original:\n' + example_strand + '\n')
    deletion_f.write('modified:\n' + new_strand + '\n')

    deletion_f.write('\n')

    simulator.err_type = 'ld'
    new_strand = simulator.inject_deletion(example_strand, del_loc)
    deletion_f.write('multiple base:\n')
    deletion_f.write('original:\n' + example_strand + '\n')
    deletion_f.write('modified:\n' + new_strand + '\n')

    deletion_f.close()


