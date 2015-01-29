def fibonacci_seq():
    """
    Iterates the Fibonacci Sequence
    """
    a, last_a = 1, 0
    while True:
        yield a
        a, last_a = last_a, a + last_a


n = 0
for f in fibonacci_seq():
    n += 1
    print('F{0} = {1}'.format(n, f))
    if len(str(f)) >= 3:
        break