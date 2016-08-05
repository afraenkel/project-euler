
from __future__ import print_function

# find all such numbers such that a1a2a3...aN = sum(aK)^5
# the left size grows much faster than the right side (exp vs poly)
# and 999,999 > 9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5 = 354294
# so it's enough to check numbers < 1,000,000

fifth_powers = {str(x):x**5 for x in range(10)}

def sum_of_fifth_pows(d):
    return sum(fifth_powers[x] for x in str(d))

if __name__ == '__main__':
    s = 0
    for d in range(2, 10**6):
        if d == sum_of_fifth_pows(d):
            s += d

    print(d)
