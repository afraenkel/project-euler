#!/usr/bin/env python

import numpy as np

def cnt_black(N):
    R = np.array([[0,1],[-1,0]])
    v = np.array([1,0])
    pos = np.array([0,0])
    colored = set()
    for step in range(N):
        t = tuple(pos)
        try:
            colored.remove(t)
            v = np.dot(R, v)
            pos = pos + v
        except KeyError:
            colored.add(t)
            v = np.dot(-1*R, v)
            pos = pos + v
    return len(colored)

if __name__ == '__main__':
    print(cnt_black(10**8))
