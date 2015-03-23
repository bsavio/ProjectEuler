"""
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from lib import gcd


def join_digits(tens, ones):
    return tens * 10 + ones


def main():
    fraction_pairs = []
    fractions = []
    for d in range(1, 10):
        for n in range(1, d):
            n_over_d = n / d
            if n_over_d >= 1:
                continue
            for cancelled in range(1, 10):
                numerator = join_digits(cancelled, n)
                denominator = join_digits(cancelled, d)
                if numerator / denominator == n_over_d:
                    fraction_pairs.append([[numerator, denominator], [n, d]])
                    fractions.append([numerator, denominator])
                numerator = join_digits(cancelled, n)
                denominator = join_digits(d, cancelled)
                if numerator / denominator == n_over_d:
                    fraction_pairs.append([[numerator, denominator], [n, d]])
                    fractions.append([numerator, denominator])
                numerator = join_digits(n, cancelled)
                denominator = join_digits(cancelled, d)
                if numerator / denominator == n_over_d:
                    fraction_pairs.append([[numerator, denominator], [n, d]])
                    fractions.append([numerator, denominator])
                numerator = join_digits(n, cancelled)
                denominator = join_digits(d, cancelled)
                if numerator / denominator == n_over_d:
                    fraction_pairs.append([[numerator, denominator], [n, d]])
                    fractions.append([numerator, denominator])
    result_fraction = [1, 1]
    for fraction in fractions:
        result_fraction[0] *= fraction[0]
        result_fraction[1] *= fraction[1]
    result_gcd = gcd(result_fraction[0], result_fraction[1])
    print(result_fraction[1] / result_gcd)

if __name__ == '__main__':
    main()