import primes as p

def main():
    s = 0
    for k in p.primes():
        if k < 2*10**6:
            s += k
        else:
            break
    return s

if __name__ == '__main__':
    print(main())
