"""
Double-base palindromes
Problem 36
The decimal number, 585 = 1001001001(base-2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from timeit import default_timer
from lib import number_to_digits


def get_base_two_digits(i):
    base_two_digits = []
    while i:
        base_two_digits.append(int(i & 1 == 1))
        i >>= 1
    return base_two_digits


def main():
    result = 0
    for n in range(1, 1000000, 2):
        base_ten_digits = number_to_digits(n)
        if base_ten_digits == base_ten_digits[::-1]:
            base_two_digits = get_base_two_digits(n)
            if base_two_digits == base_two_digits[::-1]:
                result += n
    print(result)

if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))