"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import lib


def get_narcissistic_numbers_of_power(power):
    sum_of_powers = []
    for i in range(2, 10 ** (power + 1)):
        sum_of_power = 0
        for d in lib.number_to_digits(i):
            sum_of_power += d ** power
        if sum_of_power == i:
            sum_of_powers.append(i)
    return sum_of_powers

results = get_narcissistic_numbers_of_power(5)
print(results)
print(sum(results))
