
# find the one millionth Lexicographic permutations of 0, 1, ..., 9

# Use "permutation base expansion":
# 10**6 = 2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 2*2! + 0*1!
# => [2,6,6,2,5,1,2,2,0] (zero indexed elements from succesive elements you can
# draw from at each stage


def get_lex_perm(k, charString):
    '''get's the (0-indexed) kth permutation of charString in Lexicographic order.'''
    from math import factorial
    n = len(charString)
    C = list(sorted(x for x in charString))
    
    if k > factorial(n):
        raise ValueError("index exceeds number of permutations")
    else:
        x, L = 0, []
        for j in range(n-1, 0, -1):
            J = factorial(j)
            for i in range(j+1):
                if x + (i + 1)*J >= k:
                    x += i*J
                    L.append(i)
                    break
    print(L)
    return ''.join([C.pop(k) for k in L] + C)

if __name__ == '__main__':
    print(get_lex_perm(10**6-1, '0123456789'))
