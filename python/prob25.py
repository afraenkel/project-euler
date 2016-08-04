
from __future__ import print_function

from fibonacci import fibonacci_seq


def main():
    for k, x in enumerate(fibonacci_seq(1, 1)):
        if len(str(x)) >= 1000:
            return k+1


if __name__ == '__main__':
    main()
