def is_palindromic(digits):
    count = len(digits) - 1
    n = count
    while n >= count // 2:
        if digits[n] != digits[count - n]:
            return False
        n -= 1
    return True


x = [1, 0, 1]
print(x == x[::-1])
x = [2, 1, 0, 1]
print(x[::-1])
