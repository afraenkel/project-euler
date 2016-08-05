
# Let E(x0, y0) be the number of steps it takes to determine
# the greatest common divisor of x0 and y0 with Euclid's algorithm.

# Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
# We have S(1) = 1, S(10) = 221 and S(100) = 39826.

# Find S(5·10^6).


def gcd_steps(a, b):
    k = 0
    while b:
        a, b = b, a%b
        k += 1
    return k, a


def E(a,b):
    return gcd_steps(a,b)[0]


# This starts getting slow at n=1000
# Use the fact that:
# (1) E(a,b) = E(b,a)    (obvious)
# (2) E(a,b) = E(ka, kb) for all a,b,k  (clear from euclid algo)

# partition plane into pieces generated using above relations.
def S(n):
    d = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            d += E(x,y)

    return d
