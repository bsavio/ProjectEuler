"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from lib import is_prime

maxResult = 1
for n in range(1, 20):
    if is_prime(n):
        maxResult *= n
maxResult *= 2
maxResult *= 2
maxResult *= 2
maxResult *= 3
print(maxResult)

for n in range(1, 20):
    if maxResult % n != 0:
        print(n)

#698377680
#232,792,560
#232,792,560
