

from numpy import product

def main():
    with open('resources/prob8') as f:
        L = [int(y) for line in f.read() for y in line.strip()]
        return max(map(product, zip(L,L[1:],L[2:],L[3:])))

if __name__ == '__main__':
    print(main())
    
