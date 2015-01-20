from math import sqrt


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
            divs.append(int(x/n))
    return divs

divs = get_divisors(4, False)
print(divs)
print(sum(divs))
print()
divs = get_divisors(16, False)
print(divs)
print(sum(divs))