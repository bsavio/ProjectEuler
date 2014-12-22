"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

str_n = str(2 ** 1000)
i = 0
result = 0
while(i < len(str_n)):
    result += int(str_n[i])
    i += 1

print(result)