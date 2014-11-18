"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt, ceil
from lib import is_prime, iterate_odd

number = 600851475143
limit = ceil(sqrt(number))
pf = []
for n in range(3, limit):
    if number % n == 0 and is_prime(n):
        pf.append(n)

print(max(pf))