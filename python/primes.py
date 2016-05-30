import itertools as it

def primes():
    '''Sieve of Eratosthenes'''
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

            
def prime_factors(n):
    factors = []
    p = primes()
    prime_list = [next(p) for _ in range(n+1)]
    while n > 1:
        for x in prime_list:
            if n % x == 0:
                factors.append(x)
                n = n // x
                break
    return factors
