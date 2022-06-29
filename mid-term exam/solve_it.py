def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    index = 0
    while (True):
        if test(index) or test(-index):
            return index
        index += 1


def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))