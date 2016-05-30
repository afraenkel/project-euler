
def main(n):
    sumofsq = n*(n+1)*(2*n+1)/6
    sqofsum = (n*(n+1)/2)**2
    return sqofsum - sumofsq

if __name__ == '__main__':
    main(100)
