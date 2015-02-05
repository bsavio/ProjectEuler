"""
Quadratic Primes
Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40,
40^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0
"""

from lib import is_prime

def count_quandratic_primes(a, b):
    count = 0
    n = 0
    while n == count:
        count += int(is_prime(n ** 2 + a * n + b))
        n += 1
    return count


max_n = 0
max_i = 0
max_j = 0
for i in range(-999, 1000):
    if not is_prime(abs(i)):
        continue
    for j in reversed(range(-999, 1000)):
        if not is_prime(abs(j)):
            continue
        n_count = count_quandratic_primes(i, j)
        if max_n < n_count:
            max_n = n_count
            max_i = i
            max_j = j

print(max_i * max_j)
