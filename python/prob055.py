'''Lychrel numbers'''

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def not_lychrel(x, cutoff=50):
    """returns number of iteration for a number
    to become a palindrome -- else returns 0"""
    for k in range(cutoff):
        x += int(str(x)[::-1])
        if is_palindrome(x):
            return k+1
    return 0

def main():
    H = (not_lychrel(x) for x in range(1, 10000))
    return len([x for x in H if x == 0])

if __name__ == '__main__':
    print(main())
