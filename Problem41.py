"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from timeit import default_timer
import lib


def generate_pandigitals(pandigital_length):
    seed_set = []
    for i in range(1, pandigital_length + 1):
        seed_set.append(i)
    pandigitals = []
    for pandigital in lib.lexicographic_permutations(seed_set):
        if pandigital[0] % 2 != 0 and pandigital[0] != 5:
            pandigitals.append(lib.digits_to_number(pandigital))
    return pandigitals


def main():
    pandigital_length = 9
    while pandigital_length > 1:
        pandigitals = generate_pandigitals(pandigital_length)
        pandigitals.sort(reverse=True)
        for pandigital in pandigitals:
            if lib.is_prime(pandigital):
                print(pandigital)
                pandigital_length = 0
                break
        pandigital_length -= 1
    return 0


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))