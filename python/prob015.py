
'''
Lattice paths:
paths on an NxN lattice have 2N choices of Right/Down
'''

import scipy

def main():
    return scipy.special.binom(40,2)

if __name__ == '__main__':
    main()
