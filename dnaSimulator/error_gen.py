# Module: error_gen.py

import random
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


"""
Testing:
"""

'''
if __name__ == '__main__':
    f = open('workfile', 'w')
    for j in range(1000):
        result = generate_error_type({'d': 0.1, 'i': 0.2, 's': 0.1, 'n': 0.6})
        result_to_write = str(result) + '\n'
        f.write(result_to_write)

    f.close()

    f = open('workfile', 'r')
    hist = [['d', 0], ['s', 0], ['i', 0], ['n', 0]]
    lines = f.readlines()
    for line in lines:
        if line == 'd\n':
            hist[0][1] += 1
        if line == 's\n':
            hist[1][1] += 1
        if line == 'i\n':
            hist[2][1] += 1
        if line == 'n\n':
            hist[3][1] += 1

    a_file = open('analysis', 'w')
    a_file.write('d appearance rate: ' + str(hist[0][1] / 1000) + '\n')
    a_file.write('s appearance rate: ' + str(hist[1][1] / 1000) + '\n')
    a_file.write('i appearance rate: ' + str(hist[2][1] / 1000) + '\n')
    a_file.write('n appearance rate: ' + str(hist[3][1] / 1000) + '\n')
'''





