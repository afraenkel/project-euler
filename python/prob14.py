

def collatz(seed):
    yield seed
    while seed > 1:
        if seed % 2:
            seed = 3*seed + 1
            yield seed
        else:
            seed = seed // 2
            yield seed

def main():
    return max(range(10**6), key=lambda x:len([y for y in collatz(x)]))


if __name__ == '__main__':
    main()
