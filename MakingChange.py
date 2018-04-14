__author__ = 'amitr'

import collections
import functools
import time
import numpy as np

class memoized(object): # taken from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


def ChangeCoins(AvailableCoins,Cash):
    """
    Finding the subsequence of `seq` which adds to the highest sum.

    `seq` is a sequence of integers (inc. negative).

    Return a pair whose first element is the sum of the best subsequence,
    and whose second element is the subsequence itself.

    >>> seq = [1, 4, -2, -6, -3, 8, -1, 2, -4, 4, -3]
    >>> MaxSubSequence(seq)
    9
    """

    # Return the value of the most valuable subsequence ending at
    # the j-th element of seq.
    @memoized
    def bestvalue(j):
        if j <= 1:
            return seq[0]
        else:
            return max(seq[j-1], bestvalue(j-1) + seq[j-1])

    ans = -float("inf")
    for i in range(len(seq)):
        ans = (bestvalue(i) if ans < bestvalue(i) else ans)
    return ans

seq = np.random.randint(10,size=1000)-5
seq = seq.tolist()
t = time.time()
print MaxSubSequence(seq)
print "caclulation took", time.time()-t, "sec"