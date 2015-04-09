"""
Circular primes
Problem 35
The number 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from lib import is_prime


def main():
    circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    for i in range(101, 1000000, 2):
        n = i
        digit_count = 0
        while n > 0:
            if n % 5 == 0 or n % 2 == 0:
                digit_count = -1
                break
            n //= 10
            digit_count += 1
        if digit_count == -1 or i in circular_primes or not is_prime(i):
            continue
        rotated_primes = [i]
        n = (i % 10 * 10 ** (digit_count - 1)) + (i // 10)
        while n != i:
            if not is_prime(n):
                break
            rotated_primes.append(n)
            n = (n % 10 * 10 ** (digit_count - 1)) + (n // 10)
        else:
            circular_primes += rotated_primes
    print(len(circular_primes))


from timeit import default_timer

if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))