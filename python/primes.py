

def prime_factors(n):
    factors = []
    while n > 1:
        for x in range(2, n + 1):
            if n % x == 0:
                factors.append(x)
                n = n // x
                break
    return factors
