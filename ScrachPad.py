def iterate_integer_digits(n):
    """
    Iterates digits of integers
    :param n:
    """
    while n > 0:
        yield n % 10
        n = int(n/10)


for d in iterate_integer_digits(12345):
    print(d)