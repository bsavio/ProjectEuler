"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from lib import is_prime

p = [2]
p_sum = 2
max_n = 2000000

for n in range(3, max_n, 2):
    if is_prime(n):
        p.append(n)
        p_sum += n

print(p_sum)