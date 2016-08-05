
from __future__ import print_function
import itertools as it


def make_grid(N):

    move_dict = [
        lambda x,y: (x+1,y),
        lambda x,y: (x,y-1),
        lambda x,y: (x-1,y),
        lambda x,y: (x,y+1)
        ]
    
    loc = (0,0)    
    D = {loc: 0}
    t = 1

    step_dists = it.zip_longest(
        it.count(1, 2),
        it.count(1, 2),
        it.count(2, 2),
        it.count(2, 2)
    )

    for x in step_dists:
        if x[0] >= N:
            break

        for d, f in zip(x, move_dict):
            for _ in range(d):
                loc = f(*loc)
                D[loc] = t
                t += 1

    return D


def print_grid(size=10):
    D = make_grid(size)
    for x in it.groupby(
            sorted(D, key=lambda x: (-1*x[1], x[0])),
            lambda x:x[1]
    ):
        row = '|'.join([ '%3d' % D[y] for y in x[1]])
        print('%s' %row)

if __name__ == '__main__':
    D = make_grid(1000)
    N = sum(x for (k,x) in D.items() if (sum(k) == 0 or k[0] == k[1]))
    print(N)
