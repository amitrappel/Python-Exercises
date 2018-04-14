__author__ = 'amitr'

import numpy as np

def CutRod(p,n):
    if n==0:
        return 0
    q = float("-inf")
    for i in np.arange(n)+1:
        q = np.maximum(q, p[i-1] + CutRod(p,n-i))
    return q

p = [1,5,8,9,10,7,17,20,24,30]
n = 10
print CutRod(p,n)