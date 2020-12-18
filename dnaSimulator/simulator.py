# Module: simulator.py

import strand_error_sim
import copy
from scipy.stats import skewnorm


class Simulator:
    """
    Simulator class.
    Holds the attributes needed for error simulation on a single strand:

    Class variables:
    :var self.total_error_rates: Dictionary of the total error rates used in the simulation, as provided in error_rates
        parameter.
    :var self.base_error_rates: Error rates corresponding to each base, as passed.
    :var self.long_deletion_length_rates: Based on (excluding single base deletion):
        https://www.biorxiv.org/content/biorxiv/early/2019/11/13/840231/F12.large.jpg?width=800&height=600&carousel=1
    :var self.input_path: Path of input file, as passed.
    :var self.is_stutter_method: Indicates whether simulator should use stutter method or not.
    """
    def __init__(self, total_error_rates, base_error_rates, input_path, is_stutter_method=False):
        """
        :param total_error_rates: Dictionary of the total error rates used in the simulation.
            Example of a dictionary:
            {'d': 0.1, 'i': 0.2, 's': 0.1, 'ld': 0.6}
            NOTE: Dictionary can be passed with values as strings, as the constructor can to parse them to floats.
        :param base_error_rates: Dictionary of dictionaries for each base.
            Example:
            {   'A': {'s': 0.1, 'i': 0.2, 'pi': 0.1, 'd': 0.05, 'ld': 0.6},
                'T': {...},
                'C': {...},
                'G': {...}
            }
            NOTE: Dictionary can be passed with rates values as strings, as the constructor can to parse them to floats.
        :param input_path: path of the input file.
            Example of input file content:
            TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC\n
            TGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGT\n
            AAATTTGCAACCAGAAATTTGCAACCAGAATTCACTAGAGGACGCACGCTCTATTTCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC\n
            TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC\n
            TTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCC\n
        :param is_stutter_method: False by default, set to True if stutter method should be used instead of other
            methods.
            Note: other methods have the same error simulation algorithm but with different rates, therefore
            no other statements are needed except the rates.
        """
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

    def simulate_errors(self, report_func):
        """
        Simulates strands duplication with errors on the strands from the input file.
        Writes the output in HeadEvyaLuis.txt file in the following format:
            [original strand][\n]
            *****************************[\n]
            [copy][\n]
            [copy][\n]
            ...
            [copy][\n]
            [\n]
            [\n]
            [original strand][\n]
            *****************************[\n]
            [copy][\n]
            [copy][\n]
            ...
            [copy][\n]

            ...
        """

        # count num of origin strands, each line is a separate strand:
        num_values = 0
        with open(self.input_path, 'r') as input_f:
            for line in input_f:
                num_values += 1

        # generate number of copies for each strand, as the number of strands:
        # https://stackoverflow.com/questions/24854965/create-random-numbers-with-left-skewed-probability-distribution
        max_value = 499
        skewness = 10  # Negative values are left skewed, positive values are right skewed.
        random = skewnorm.rvs(a=skewness, loc=max_value, size=num_values)  # Skewnorm function
        random = random - min(random)  # Shift the set so the minimum value is equal to zero.
        random = random / max(random)  # Standardize all the values between 0 and 1.
        random = random * max_value  # Multiply the standardized values by the maximum value.
        random = random + 1  # avoid 0
        random = [int(x) for x in random]  # convert to integers

        # for each strand, copy it the corresponding generated number of times and simulate error on each copy:
        i = 0
        with open(self.input_path, 'r') as input_f:
            with open('HeadEvyaLuis.txt', 'w') as output_f:
                for line in input_f:
                    report_func(num_values, i)
                    # write ORIGINAL strand with divider first:
                    original_strand = line
                    # strip the strand from newline:
                    original_strand = original_strand.rstrip()
                    output_f.write(original_strand + '\n' + '*****************************\n')

                    # for each strand, do the simulation on a copy of it random[i] (the generated number of copies) times:
                    for j in range(random[i]):

                        # duplicate strand to create a working (output) strand:
                        output_strand = copy.deepcopy(original_strand)
                        # create a strand simulator for it:
                        strand_error_simulator = strand_error_sim.StrandErrorSimulation(self.total_error_rates,
                                                                                        self.base_error_rates,
                                                                                        self.long_deletion_length_rates,
                                                                                        output_strand)
                        # simulate according to method:
                        if self.is_stutter_method:
                            output_strand = strand_error_simulator.simulate_stutter_errors_on_strand()
                        else:
                            output_strand = strand_error_simulator.simulate_errors_on_strand()

                        # write the output strand to file:
                        output_f.write(output_strand + '\n')

                    # after each strand, add 2 newlines:
                    output_f.write('\n\n')

                    i += 1

def parse_rate(rate_str) -> float:
    """
    Parses string of a single string of a numeric value representing a rate.
    If the parameter is already a float, does nothing (and returns it).
    :param rate_str: Can be either:
        - a number, eg. '0.053'
        or
        - use 10^x exp, eg. '53E-4' (which is equivalent to 0.053 or 53 * 10^(-4))
        NOTE: it can be a float as well, in this case it will simply be returned.
    :return: The float value of the given string.
        NOTE: If a float is passed as argument, it'll be returned as-is.
    """
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
    """
    Parses dictionary's rates to floats if they appear as strings.
    Handles both "one level" and "two level" dictionaries used in the simulator.
    Modifies the passed dictionary!
    :param rates_dict: The dictionary to parse.
    """
    for key, value in rates_dict.items():
        if isinstance(value, dict):  # the given dictionary is a base error rates dictionary
            # key is the base, value is the dictionary for the base, consisting of errors & rates.
            for error, rate in value.items():
                rates_dict[key][error] = parse_rate(rate)
        else:  # the given dictionary is a one-level dictionary, assuming there are no more types of dictionaries.
            rates_dict[key] = parse_rate(value)


# Testing:
#
# if __name__ == '__main__':
#
#     error_rates_example = {'d': 9.58 * (10 ** (-4)),
#                            'ld': 2.33 * (10 ** (-4)),
#                            'i': 5.81 * (10 ** (-4)),
#                            's': 1.32 * (10 ** (-3))}
#     base_error_rates_example = {'A':
#                                 {'s': 0.135 * (10**(-2)),
#                                  'i': 0.057 * (10**(-2)),
#                                  'pi': 0.059 * (10**(-2)),
#                                  'd': 0.099 * (10**(-2)),
#                                  'ld': 0.024 * (10**(-2))},
#                                 'C':
#                                     {'s': 0.135 * (10 ** (-2)),
#                                      'i': 0.059 * (10 ** (-2)),
#                                      'pi': 0.058 * (10 ** (-2)),
#                                      'd': 0.098 * (10 ** (-2)),
#                                      'ld': 0.023 * (10 ** (-2))},
#                                 'T':
#                                     {'s': 0.126 * (10 ** (-2)),
#                                      'i': 0.059 * (10 ** (-2)),
#                                      'pi': 0.057 * (10 ** (-2)),
#                                      'd': 0.094 * (10 ** (-2)),
#                                      'ld': 0.023 * (10 ** (-2))},
#                                 'G':
#                                     {'s': 0.132 * (10 ** (-2)),
#                                      'i': 0.058 * (10 ** (-2)),
#                                      'pi': 0.058 * (10 ** (-2)),
#                                      'd': 0.096 * (10 ** (-2)),
#                                      'ld': 0.023 * (10 ** (-2))}}
#
#     input_path_example = 'input.txt'
#
#     sim = Simulator(error_rates_example, base_error_rates_example, input_path_example)
#
#     sim.simulate_errors()
#
#     sim = Simulator(error_rates_example, base_error_rates_example, input_path_example, True)
#
#     sim.simulate_errors()



