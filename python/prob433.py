
import itertools as it
# Let E(x0, y0) be the number of steps it takes to determine
# the greatest common divisor of x0 and y0 with Euclid's algorithm.

# Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
# We have S(1) = 1, S(10) = 221 and S(100) = 39826.

# Find S(5·10^6).

def E(a, b):
    k = 0
    while b:
        a, b = b, a%b
        k += 1
    return k


N = 10
lens = (x for k in it.count(1) for x in it.repeat(k,2))
cols = it.count(2)
d = 0    
for c,l in zip(cols, lens):
    first_row = 2*c - l
    if first_row > N:
        break
    for r in range(first_row, first_row + l):
        if r > N:
            break
        f = (r-c)
        incr = 0
        while (r+incr) <= N:
            d += E(r, c)*( (N-c-incr)//(c+incr)  )
            incr += f
    d += (N - r + 1) // c

d += (N-1)
d *= 2
d += (N-1)*N//2
d += N

print(d)
# This starts getting slow at n=1000
# Use the fact that:
# (1) E(a,b) = E(b,a)    (obvious)
# (2) E(a,b) = E(ka, kb) for all a,b,k  (clear from euclid algo)
# above is not enough

# probably compute a bunch of gcd steps at each step using memoizing


def S(n):
    d = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            d += E(x,y)

    return d

