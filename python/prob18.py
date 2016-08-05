
from __future__ import print_function
import functools as ft

#  a b c
# d e f g

# use the fact that the largest path sum at row N only
# depends on the path sums computed to the row before.

def get_default(L, idx, default=0):
    try:
        return L[idx]
    except:
        return default

    
def fold_dist(L1, L2):
    if len(L2) - len(L1) != 1:
        raise ValueError("input lists are wrong size")
    
    for k, x in enumerate(L2):
        L2[k] += max(get_default(L1, k-1), get_default(L1, k))

    return L2


def largest_path_sum(T):
    """T is a triangular list of lists."""
    return max(ft.reduce(fold_dist, T))


def create_input():
    L = """75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    T = []
    for line in L.split('\n'):
        T.append(list(map(lambda x: int(x), line.split())))
        
    return T

def create_rand_input(N, r):
    '''N = number of rows, r = max size of positive integer entries '''
    from random import randint
    T = []
    for x in range(1, N):
        t = []
        for _ in range(x):
            t.append(randint(1,r))
        T.append(t)
    return T
    

if __name__ == '__main__':
    T = create_input()
    print(largest_path_sum(T))
