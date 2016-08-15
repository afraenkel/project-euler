#!/usr/bin/env python

from __future__ import print_function
import sys
import os

N = int(os.environ['N'])

def E(a, b):
    k = 0
    while b:
        a, b = b, a%b
        k += 1
    return k

for line in sys.stdin:
    c = int(line.strip())
    d = 0
    if 2*c < N:
        for i in range(1, c + 1):
            d += E(c + i, c)*((N - i)//c)
    else:
        for r in range(c + 1, N + 1):
            d += E(r, c)
        
    print('%d\t%d' %(1,d))
