"""
Sub-string divisibility
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from timeit import default_timer
import lib


def main():
    primes = [17, 13, 11, 7, 5, 3, 2]
    result = 0
    for pandigital in lib.lexicographic_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        for i in reversed(range(3, 10)):
            sub = lib.digits_to_number(pandigital[i - 3:i])
            to_test = sub / primes[i - 3]
            if to_test != int(to_test):
                break
        else:
            result += lib.digits_to_number(pandigital)
    print(result)
    return 0


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))