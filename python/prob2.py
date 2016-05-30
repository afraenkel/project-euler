import fibonacci as fib

def main(N):
    fibseq = fib.fibonacci_seq(1,1)
    k, s = next(fibseq), 0
    while k < N:
        if not k % 2:
            s += k
        k = next(fibseq)
    return s

if __name__ == '__main__':
    main(4*10**6)
