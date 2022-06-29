from itertools import *
import time
import random

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


# More efficient algorithm for the powerset generator
def powerSet2(items):
    # powerSet([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    return chain.from_iterable(combinations(items, r) for r in range(len(items)+1))


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

    __repr__ = __str__


# build a list of n items of various weights and values
def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]


# determine average running time of powerset with n items
def timePowerSet(n,ntrials=10):
    # time how long it takes to run powerset
    def howLong(items):
        start = time.clock()
        pset = powerSet2(items)
        for item in pset:
            pass
        stop = time.clock()
        return stop - start

    # run the specified number of trials
    times = [howLong(buildRandomItems(n))
             for i in range(ntrials)]

    print('Average running time was', sum(times) / ntrials, 'seconds.')


timePowerSet(16)
