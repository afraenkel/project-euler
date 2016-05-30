from math import sqrt
from functools import reduce
import itertools as it

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))


def triangular():
    for x in it.count(1):
        yield int(x*(x+1)/2)

def main():
    for t in triangular():
        if len(factors(t)) > 500:
            return t

if __name__ == '__main__':
    print(main())
