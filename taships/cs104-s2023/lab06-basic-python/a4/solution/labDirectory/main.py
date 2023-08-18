'''
    Sieve of Eratosthenes
'''

import sys
from functools import reduce

num = int(sys.argv[1])
print(sorted(list(reduce(set.intersection, map(
    lambda t : set(filter(
        lambda s : s == t or s % t != 0, range(2, num+1)
    )), range(2, num+1)
)))))
