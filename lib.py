from math import sqrt, ceil

def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def fibonacci_seq():
    """
    Iterates the Fibonacci Sequence

    """
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def iterate_even(n, iterable):
    """
    Iterates only n even numbers from the iterable
    :param n:
    :param iterable:
    :return:
    """
    for i in iterable:
        if i >= n:
            return
        if i % 2 == 0:
            yield i


def iterate_odd(n, iterable):
    """
    Iterates only odd numbers from the iterable
    :param n:
    :param iterable:
    :return:
    """
    for i in iterable:
        if i >= n:
            return
        if i % 2 != 0:
            yield i


def is_prime(n):
    """
    Checks if a number is prime
    :param n: the number to check
    :return: True if prime, False otherwise
    """
    if n <= 2 or is_even(n):
        return n == 2
    limit = ceil(sqrt(n))
    for x in iterate_odd(limit - 3, range(3, limit)):
        if n % x == 0:
            return False
    return True

