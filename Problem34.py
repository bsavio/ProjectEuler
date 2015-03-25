"""
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial
from timeit import default_timer


def get_factorials():
    factorials = [0] * 10
    for i in range(0, 10):
        factorials[i] = factorial(i)
    return factorials


def main():
    factorials = get_factorials()
    result = 0
    for i in range(10, factorials[9] * 7):
        factorial_sum = 0
        d = i
        while d > 0:
            factorial_sum += factorials[d % 10]
            d //= 10
        if factorial_sum == i:
            result += i
    print(result)


if __name__ == '__main__':
    start = default_timer()
    main()
    elapsed_time = (default_timer() - start) * 1000
    print(u"Runtime: {0} ms".format(elapsed_time))