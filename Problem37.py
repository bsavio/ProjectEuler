"""
Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from timeit import default_timer
import lib


def main():
    truncatable_primes = []
    invalid_middle_digits = {2, 4, 5, 6, 8}
    invalid_end_digits = {1, 4, 6, 8, 9}
    primes = [2, 3, 5, 7, 11, 13]
    n = 11
    while len(truncatable_primes) < 11:
        candidate_digits = lib.number_to_digits(n)
        digit_count = len(candidate_digits)
        # Skip any number that has even digits or 5 in any places accept the first or last digit
        if (len(invalid_middle_digits & set(candidate_digits[:-1])) > 0
            or candidate_digits[digit_count - 1] in invalid_end_digits
            or candidate_digits[0] in invalid_end_digits
            or not lib.is_prime_cached(n, primes)):
            n += 2
            continue
        for i in range(1, digit_count):
            truncated_right = lib.digits_to_number(candidate_digits[i::])
            if not lib.is_prime_cached(truncated_right, primes):
                break
            truncated_left = lib.digits_to_number(candidate_digits[:digit_count - i:])
            if not lib.is_prime_cached(truncated_left, primes):
                break
        else:
            truncatable_primes.append(n)
        n += 2
    print(truncatable_primes)
    print(sum(truncatable_primes))


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))