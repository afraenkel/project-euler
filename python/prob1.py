

def main(N):
    return sum(x for x in range(N) if not x % 3 or not x % 5)

if __name__ == '__main__':
    main(1000)
