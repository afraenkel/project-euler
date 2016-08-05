#!/usr/bin/env python

from __future__ import print_function

abundants = {}
def is_abundant(n):
    '''returns a list of all divisors of a number n > 0'''
    global abundants
    try:
        return abundants[n]
    except KeyError:
        ab = sum(x for x in range(1, n) if n % x == 0) > n
        abundants[n] = ab
        return ab

    
def main():
    '''the sum of all the positive integers which cannot be written as the sum of two abundant numbers'''
    # it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
    L = []
    for x in range(28123):
        for y in range(x // 2):
            if is_abundant(y) and is_abundant(x-y):
                break
            elif y == (x // 2) - 1:
                L.append(x)
    return sum(L)


if __name__ == '__main__':
    main()
