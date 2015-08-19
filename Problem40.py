"""
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from timeit import default_timer


def main():
    irrational = '.'
    i = 1
    while len(irrational) < 1000001:
        irrational = ''.join([irrational, str(i)])
        i += 1
    result = 1
    for n in range(0, 7):
        result *= int(irrational[10 ** n])
    print(result)
    return 0


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))