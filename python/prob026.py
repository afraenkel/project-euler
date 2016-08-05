
from __future__ import print_function

import itertools as it

# find the largest repeating cycle in the decimal
# expansion of 1/d where 0 < d < 1000

def decimal_cycle_length(d):
    dividend = 10*(1 - (1//d)*d)
    decimals, dividends = [], []
    for k in it.count(1):
        decimals.append(dividend // d)
        dividends.append(dividend)
        
        dividend = 10*(dividend - (dividend // d)*d)
        if dividend in dividends:
            idx = dividends.index(dividend)
            break
    return len(decimals[idx:])

if __name__ == '__main__':
    M = max(decimal_cycle_length(x) for x in range(1, 1000))
    print(M)
