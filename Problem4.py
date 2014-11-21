"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

pals = []
for x in reversed(range(100, 999)):
    for y in reversed(range(100, x)):
        xy = str(x * y)
        if xy == xy[::-1]:
            pals.append(x * y)
print(max(pals))


def is_palindrome(number):
    """
    Tests if a number is a palindrome
    :type number: int
    :param number:
    :return:
    """
    str_input = str(number)
    return str_input == reversed(str_input)