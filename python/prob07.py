
import primes as pr

if __name__ == '__main__':
    for k, p in enumerate(pr.primes()):
        if k == 10001:
            print(p)
            break
