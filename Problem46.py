"""
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a
square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from timeit import default_timer
import lib


def is_prime_cached(n, primes):
    """
    Checks if a number is prime. Caches primes found in primes
    :param n: the number to check
    :param primes: list of known primes
    :return: True if prime, False otherwise
    """
    if n in primes:
        return True
    if lib.is_prime(n):
        primes.add(n)
        return True
    return False


def main():
    primes = set()
    result = None
    n = 1
    while not result:
        n += 2
        if is_prime_cached(n, primes):
            continue
        is_goldbach_other = False
        for p in primes:
            to_test = ((n - p)/2)**0.5
            if to_test > 0 and to_test.is_integer():
                is_goldbach_other = True
                break
        if not is_goldbach_other:
            result = n
    print(n)
    return 0


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))