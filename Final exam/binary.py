import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    choices_array = np.array(choices)
    totals = []
    for number in range(2**len(choices)):
        binary_string = bin(number)[2:]
        zeros = ""
        for _ in range(len(choices)-len(binary_string)):
            zeros += "0"
        binary = zeros + binary_string
        binary_list = []
        for digit in binary:
            binary_list.append(int(digit))
        array = np.array(binary_list)
        totals.append(array)

    best = totals[0]
    for array in totals:
        multDifference = total - sum(choices_array*array)
        if (not multDifference < 0) and multDifference < total - sum(best*choices_array):
            best = array
        elif (not multDifference < 0) and multDifference == total - sum(best * choices_array):
            if sum(array) < sum(best):
                best = array
    return best


choices = [10, 100, 1000, 3, 8, 12, 38]
total = 1171
print(repr(find_combination(choices, total)))
