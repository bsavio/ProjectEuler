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
    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def find_pythagorean_triplet(a, b, c, perimeter):
    """
    Finds the the pythagorean triplet for the given perimeter.
    Pass a = 3, b = 4, c = 5 to start
    :param a:
    :type b: int
    :param b:
    :type a: int
    :param c:
    :type c: int
    :param perimeter:
    :type perimeter: int
    :return:
    """
    abc_sum = a + b + c
    if abc_sum > perimeter:
        return []
    if a % 10 == 0 and b % 10 == 0 and c % 10 == 0:
        print([a, b, c])
    if abc_sum == perimeter:
        return [a, b, c]
    first = find_pythagorean_triplet(a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c, perimeter)
    if len(first) == 3:
        return first
    second = find_pythagorean_triplet(a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c, perimeter)
    if len(second) == 3:
        return second
    third = find_pythagorean_triplet(-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c, perimeter)
    if len(third) == 3:
        return third
    return []


def primitive_pythagorean_triples():
    """
    Iterates all primitive Pythagorean Triples
    """
    m = 2
    while True:
        for n in range(1, m):
            yield [m**2 - n**2, 2*m*n, m**2 + n**2]
        m += 1
