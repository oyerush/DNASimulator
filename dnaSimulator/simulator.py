# Module: simulator.py

import strand_error_sim
import copy

# Simulator class.
# Holds the attributes needed for error simulation on a single strand:
# PARAMS:
# @ total_error_rates - dictionary of the total error rates used in the simulation.
#       Example of a dictionary:
#       {'d': 0.1, 'i': 0.2, 's': 0.1, 'ld': 0.6}
# @ base_error_rates - dictionary of dictionaries for each base.
#       Example:
#       {   'A': {'s': 0.1, 'i': 0.2, 'pi': 0.1, 'd': 0.05, 'ld': 0.6},
#           'T': {...},
#           'C': {...},
#           'G': {...}
#       }
# @ input_path - path of the input file.
#       Example of input file content:
#       TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC
#       TGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGT
#       AAATTTGCAACCAGAAATTTGCAACCAGAATTCACTAGAGGACGCACGCTCTATTTCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC
#       TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC
#       TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC
# @ is_stutter_method - False by default, set to True if stutter method should be used instead of other methods.
#                       Note: other methods have the same error simulation algorithm but with different rates, therefore
#                       no other statements are needed except the rates. (
#
# Class variables:
# * method - the method used,
# * total_error_rates - dictionary of the total error rates used in the simulation, as provided in error_rates
#                       parameter.
# * base_error_rates - error rates corresponding to each base, as passed.
# * long_deletion_length_rates - based on (excluding single base deletion):
#       https://www.biorxiv.org/content/biorxiv/early/2019/11/13/840231/F12.large.jpg?width=800&height=600&carousel=1
# * input_path - path of input file.
# * is_stutter_method - indicates whether simulator should use stutter method of not.
class Simulator:
    def __init__(self, total_error_rates, base_error_rates, input_path, is_stutter_method=False):
        self.total_error_rates = copy.deepcopy(total_error_rates)
        self.base_error_rates = copy.deepcopy(base_error_rates)
        parse_rates_dictionary(self.total_error_rates)
        parse_rates_dictionary(self.base_error_rates)
        self.long_deletion_length_rates = {2: 2.8 * (10 ** (-4)),
                                           3: 7.75 * (10 ** (-5)),
                                           4: 3.25 * (10 ** (-5)),
                                           5: 10 ** (-6),
                                           6: 5.5 * (10 ** (-8))}
        self.input_path = input_path
        self.is_stutter_method = is_stutter_method

    def simulate_errors(self):
        # duplicate strands to create a set of working strands:
        self.duplicate_strands()

        strands_f = open('duplicated_strands', 'r')
        output_f = open('eyyat.txt', 'r')  # TODO: Check if that's the file...?

        # read input file line by line, each line is a separate strand:
        strands = strands_f.readlines()
        for strand in strands:
            # create a strand simulator for each strand:
            strand_error_simulator = strand_error_sim.StrandErrorSimulation(self.total_error_rates,
                                                                            self.base_error_rates,
                                                                            self.long_deletion_length_rates,
                                                                            strand)
            output_strand = None
            if self.is_stutter_method:
                output_strand = strand_error_simulator.simulate_stutter_errors_on_strand()
            else:
                output_strand = strand_error_simulator.simulate_errors_on_strand()

            # write the modified strand:
            output_f.write(output_strand + '\n')

        strands_f.close()
        output_f.close()

    def duplicate_strands(self):
        output_f = open('duplicated_strands', 'w')
        input_f = open(self.input_path, 'r')

        # read input file line by line, each line is a separate strand:
        strands = input_f.readlines()
        for strand in strands:
            for i in range(100):  # TODO: Check how many copies of each strand to produce
                output_f.write(strand + '\n')

        output_f.close()
        input_f.close()


def parse_rate(rate_str) -> float:
    if isinstance(rate_str, float):
        return rate_str
    # if string is a number, convert it to float as-is.
    # if string is represented with E, convert it to a number first.
    index = rate_str.find('E')
    if index == -1:
        return float(rate_str)
    else:
        num = float(rate_str[:index])
        exp = 10 ** float(rate_str[index + 1:])
        return num * exp


def parse_rates_dictionary(rates_dict):
    for key, value in rates_dict:
        if isinstance(value, dict):  # the given dictionary is a base error rates dictionary
            # key is the base, value is the dictionary for the base, consisting of errors & rates.
            for error, rate in value:
                rates_dict[key][error] = parse_rate(rate)
        else:  # the given dictionary is a one-level dictionary, assuming there are no more types of dictionaries.
            rates_dict[key] = parse_rate(value)

