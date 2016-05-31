'''
cubic permumations
'''

import collections as c

def cubes_to_N(N):
    n = int((10**N)**(1/3))
    return {str(x**3): x for x in range(n)}

def main():
    D = cubes_to_N(15)
    sortedD = c.defaultdict(list)
    for x,y in D.items():
        sortedD[''.join(sorted(x))].append(y)

    return min(min(L) for L in sortedD.values() if len(L) == 5)

if __name__ == '__main__':
    main()
