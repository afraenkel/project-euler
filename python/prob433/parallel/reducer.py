#!/usr/bin/env python

from __future__ import print_function
import sys
import os

N = int(os.environ['N'])

d = 0
for line in sys.stdin:
    _, s = line.split('\t')
    d += int(s)

d *= 2
d += (N-1)*N//2
d += N

print(d)
