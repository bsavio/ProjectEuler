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

import re

max_rep = 0
d = 0
for i in range(1, 1000):
    num = str(round(1/i, 100))
    midway = int(len(num)/2)
    if midway < max_rep:
        continue
    i_min_rep = 0
    for j in range(1, int(len(num)/2)):
        regex = '(\d{' + str(j) + '})\\1+'
        if re.search(regex, num) is not None:
            i_min_rep = j
            break
    if i_min_rep > max_rep:
        max_rep = j
        d = i
        print(num)
        print(max_rep)
        print(d)
        print()

print('----------')
print(max_rep)
print(d)