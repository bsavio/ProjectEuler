"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import datetime
from lib import collatz_seq

start = datetime.datetime.now()
collatz_cache = [0, 1]
for i in range(2, 1000000):
    count = 0
    for n in collatz_seq(i):
        if n < i:
            count += collatz_cache[n]
            break
        count += 1
    collatz_cache.append(count)
run_time = datetime.datetime.now() - start
result_max = max(collatz_cache)
print("Result - i: {0} count: {1}".format(str(collatz_cache.index(result_max)), str(result_max)))
print("")
print(str(run_time.total_seconds()))