'''
largest exponential
'''
import math

def main():
    L = [x.strip().split(',') for x in open('./resources/prob99')]
    return sorted(L, key=lambda x: int(x[1])*math.log10(int(x[0])), reverse=True)[0]

if __name__ == '__main__':
    main()
