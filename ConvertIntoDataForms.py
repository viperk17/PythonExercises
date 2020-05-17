"""
Given an integer, , print the following values for each integer from to n:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each
from to . Each value should be space-padded to match the width of the binary value of .
"""

def print_formatted(number):
    w = len("{0:b}".format(number))
    for i in range(1,number+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)