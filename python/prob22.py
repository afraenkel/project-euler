#!/usr/bin/env python

from __future__ import print_function
import string

letter_scores = {y: (x + 1) for (x, y) in enumerate(string.ascii_uppercase)}

def names_score(loc, name):
    return loc* sum(letter_scores[x] for x in name)

def total_score(L):
    return sum(names_score(k, n) for (k, n) in enumerate(L))


if __name__ == '__main__':
    with open('resources/prob22') as f:
        L = f.read().strip().split(',')
    L = map(lambda x:x.strip('"'), L)
    score = total_score(L)
    print(score)
