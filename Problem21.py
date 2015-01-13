"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from lib import get_divisors


def d(n):
    return sum(get_divisors(n, False))

amicable_numbers = []
a = 4
while a < 10000:
    b = d(a)
    db = d(b)
    if db == a and a != b:
        if a < 10000 and a not in amicable_numbers:
            amicable_numbers.append(a)
        if b < 10000 and b not in amicable_numbers:
            amicable_numbers.append(b)
    a += 1
print(amicable_numbers)
print(sum(amicable_numbers))