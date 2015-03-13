from math import sqrt, log


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def fibonacci_seq():
    """
    Iterates the Fibonacci Sequence
    """
    a, b = 0, 1
    while True:
        yield b
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


def get_primes_in_range(a, b):
    """
    Get's a list of all primes inclusively in the range [a, b]
    :param a:
    :param b:
    :return:
    """
    primes = []
    if a % 2 == 0:
        if a == 2:
            primes.append(2)
        a += 1
    for n in range(a, b + 1, 2):
        if is_prime(n):
            primes.append(n)
    return primes


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
            yield [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]
        m += 1


def triangular_numbers():
    """
    Iterates all triangular numbers
    """
    n = 1
    result = 0
    while True:
        result += n
        yield result
        n += 1


def get_divisors(x, include_x=True):
    """
    Gets all divisors of x
    :param x:
    :param include_x: Defaults to true
    :return:
    """
    divs = [1]  # Include 1 as a divisor
    if include_x and x != 1:
        divs.append(x)  # Include x as a divisor
    if x <= 2:
        return divs
    max_n = int(sqrt(x))
    if max_n == sqrt(x):
        divs.append(max_n)
    else:
        max_n += 1
    for n in range(2, max_n):
        if x % n == 0:
            divs.append(n)
            divs.append(int(x / n))
    return divs


def count_divisors(x, include_x=True):
    """
    Counts all divisors of x
    :param x:
    :param include_x: Defaults to true
    :return:
    """
    div_count = 1 + int(include_x)  # Counting 1 as a divisor and x if include_x is true
    max_n = int(sqrt(x))
    if max_n == sqrt(x):
        div_count += 1
    else:
        max_n += 1
    for n in range(2, max_n):
        if x % n == 0:
            div_count += 2
    return div_count


def collatz_seq(n):
    """
    Iterates through the Collatz Sequence
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)
    :param n: Start of the sequence
    """
    while n >= 1:
        yield int(n)
        if n == 1:
            n = 0
        elif is_even(n):
            n /= 2
        else:
            n = 3 * n + 1


def factorial(n):
    """
    Calculates n!
    :param n:
    :return:
    """
    for i in range(1, n):
        n *= i
    return n


def combinations(n, k):
    """
    Calculates the number of combinations of choosing k of n elements
    :param n:
    :param k:
    :return:
    """
    if k == 0 or n == k:
        return 1
    return factorial(n) / (factorial(k) * factorial(n - k))


def check_perfect_abundant_deficient(n):
    """
    Determines if a number is deficient, perfect or abundant.
    :param n:
    :return: 1 if abundant, 0 if perfect and -1 if deficient
    """
    sum_of_divisors = sum(get_divisors(n, False))
    if sum_of_divisors < n:
        return -1
    if sum_of_divisors == n:
        return 0
    if sum_of_divisors > n:
        return 1


def swap_elements(iterable, i, j):
    """
    Swaps element of the list at index i with the element at index j
    :param iterable: list
    :type iterable: list
    :param i: index to swap
    :type i: int
    :param j: index to swap
    :type j: int
    """
    t = iterable[i]
    iterable[i] = iterable[j]
    iterable[j] = t


def is_perfect_power(n, primes=None):
    """
    Test if n is a perfect power. (n = a^b).
    :param n:
    :param primes: an optional list of primes.  It builds the list if not supplied.
    :return: If a perfect power then returns the smallest prime p such that n = a^p else 0
    """
    max_p = max(log(n), 2)
    if primes is None:
        get_primes_in_range(2, max_p)
    for p in primes:
        if p > max_p:
            break
        x = n ** (1/p)
        if n == x**p:
            return p
    return 0


def number_to_digits(n):
    """
    Converts a number into a list of it's digits
    :rtype : list
    :param n:
    :return: a list of digits of n
    """
    results = []
    for digit in str(n):
        results.append(int(digit))
    return results


def lexicographic_permutations(to_permute):
    """
    Generates lexicographic permutations
    :param to_permute:
    :return:
    """
    while True:
        yield to_permute
        k = -1
        # Find the right most index k such that to_permute[k} < to_permute[k+1]
        for i in reversed(range(0, len(to_permute) - 1)):
            if to_permute[i] < to_permute[i + 1]:
                k = i
                break
        #  If we found no such k then the permutations are complete
        if k == -1:
            return
        # Find the largest l such that to_compute[k] < to_compute[l]
        l = k
        for i in reversed(range(k + 1, len(to_permute))):  # to_permute[k+1:]:
            if to_permute[l] < to_permute[i]:
                l = i
                break
        #  Swap elements k and l
        swap_elements(to_permute, k, l)
        #  Reverse the order of the elements K+1 to n
        to_permute = to_permute[:k + 1] + to_permute[:k:-1]