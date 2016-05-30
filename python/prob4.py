
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def palindrome_products(N):
    for x in range(10**(N-1), 10**N):
        for y in range(x, 10**N):
            p = x * y
            if is_palindrome(p):
                yield p

def main():
    return max(x for x in palindrome_products(3))

if __name__ == '__main__':
    main()
