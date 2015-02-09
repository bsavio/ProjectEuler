"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666... and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def divide(numerator, denominator):
    num_result = numerator // denominator
    numerator = 10 * (numerator - num_result * denominator)
    result = str(num_result)
    if numerator == 0:
        return result
    result += '.'
    states = {}
    while numerator > 0:
        previous_state = states.get(numerator, None)
        if previous_state is not None:
            result = 'r' + result
            break
        states[numerator] = len(result)
        num_result = numerator // denominator
        numerator = 10 * (numerator - num_result * denominator)
        result += str(num_result)
    return result


max_d = 0
max_len = 0
for i in range(1, 1000):
    test = divide(1, i)
    if test[0] == 'r' and len(test) > max_len:
        max_d = i
        max_len = len(test)

print(max_d)
print(divide(1, max_d))