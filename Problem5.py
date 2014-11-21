"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from math import floor
from lib import is_prime, iterate_even

maxResult = 1
for n in range(1, 20):
    if is_prime(n):
        maxResult *= n
maxResult *= 2
maxResult *= 2
maxResult *= 2
print(maxResult)

for r in range(floor(maxResult/20), maxResult):
    if r % 10 != 0:
        continue
    for n in range(1, 20):
        if r % n != 0:
            break
    else:
        print(n)
        continue
print('The End!')