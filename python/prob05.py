import math
import functools

def _lcm(x, y):
    return x*y // math.gcd(x, y)

def lcm(*L):
    return functools.reduce(_lcm, L, 1)
            
if __name__ == '__main__':
    lcm(*range(1,20))
