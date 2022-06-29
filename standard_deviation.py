def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('nan')
    mean = sum(x for x in L) / float(len(L))
    return ((sum((i - mean)**2 for i in L)/len(L))**0.5)/mean


L = [10, 4, 12, 15, 20, 5]
print(stdDevOfLengths(L))

