"""
Triangular, pentagonal, and hexagonal
Problem 45
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from timeit import default_timer
import lib


def get_hexagonal(n):
    return n * (2 * n - 1)


def get_pentagonal(n):
    return (3 * (n ** 2) - n) / 2


def get_triangular(n):
    return (n * (n + 1)) / 2


def main():
    tn = 285
    pn = 165
    hn = 143  # Grows the fastest outer loop
    result_found = False
    pentagonal = get_pentagonal(pn)
    triangular = get_triangular(tn)
    while not result_found:
        hn += 1
        hexagonal = get_hexagonal(hn)
        while pentagonal < hexagonal:
            pn += 1
            pentagonal = get_pentagonal(pn)
        if pentagonal != hexagonal:
            continue
        while triangular < hexagonal:
            tn += 1
            triangular = get_triangular(tn)
        result_found = triangular == hexagonal
    print(hexagonal)
    return


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))