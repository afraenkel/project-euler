import math
import itertools as it

'''
a^2 + b^2 = c^2
a + b + c = N

a^2 + b^2 = (N - b - a)^2
a^2 + b^2 = N^2 + b^2 + a^2 - 2Nb - 2Na + 2ab
 - N^2 + 2N(a+b) - 2ab = 0
'''

def f(N):
    def closure(x,y):
        return -1*N**2 + 2*N*(x+y) - 2*x*y
    return closure

def cantor_pairing():
    '''enumerate N x N'''
    for k in it.count():
        i = int((-1 + math.sqrt(1+8*k))/2)
        yield (k-i*(1+i)/2, i*(3+i)/2-k)
    
def main():
    func = f(1000)
    for x, y in cantor_pairing():
        if func(x, y) == 0 and x and y:
            return (x, y, 1000 - x - y)
        
if __name__ == '__main__':
    print(main())
