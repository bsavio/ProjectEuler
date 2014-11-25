"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from math import sqrt

primes = [2]
n = 1
while len(primes) < 10001:
    n += 2
    is_prime = True
    for a in primes:
        if a > int(sqrt(n)):
            break
        if n % a == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(max(primes))