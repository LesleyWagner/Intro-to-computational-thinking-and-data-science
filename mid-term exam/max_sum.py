def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_sum = 0
    for i in range(len(L)):
        if L[i] > 0:
            this_sum = 0
            for j in range(i, len(L)):
                this_sum += L[j]
                if this_sum > max_sum:
                    max_sum = this_sum
    return max_sum


example = [3, 4, -8, 15, -1, 2]
print(max_contig_sum(example))
