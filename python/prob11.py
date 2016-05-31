#TODO

## function that inputs a vector and outputs largest product of 4 consecutive integers in that vector

## rows -- apply function
## cols -- transpose -> apply function
## diag -- indices whose diff=const (-n to n) -> apply row function
## anti -- indices whose sum=cons (0 to 2n) -> apply row function

import numpy as np

def maxprod(v):
    '''finds the max product of 4 consecutive entries in a vector'''
    if len(v) < 4:
        return 0
    return max(map(np.product, zip(v,v[1:],v[2:],v[3:])))

def to_diag(a, off=False):
    L = []
    for k in range(len(a)):
        if off:
            idx = list(zip(*[(i,j) for i in range(k) for j in range(k) if i-j == k]))
        else:
            idx = list(zip(*[(i,j) for i in range(k) for j in range(k) if i+j == k]))
        L.append(a[idx])
    return np.array(L)

def maxrows(a):
    '''finds the max product of 4 consective entries across rows of an array'''
    return max(map(maxprod, a))

def maxcols(a):
    return max(map(maxprod, np.transpose(a)))

def maxdiag(a):
    return max(map(maxprod, to_diag(a)))

def maxoffdiag(a):
    return max(map(maxprod, to_diag(a, off=True)))

def maxall(a):
    return max(maxrows(a), maxcols(a), maxdiag(a), maxoffdiag(a))

def main():
    L = [x.strip() for x in open('./resources/prob11')]
    a = np.array(list(map(lambda x:x.split(),L)), dtype=float)
    return maxall(a)

if __name__ == '__main__':
    print(main())
    
