"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from lib import factorial, swap_elements


def lexicographic_permutation_generator(to_permute):
    while True:
        yield to_permute
        k = -1
        # Find the right most index k such that to_permute[k} < to_permute[k+1]
        for i in reversed(range(0, len(to_permute) - 1)):
            if to_permute[i] < to_permute[i + 1]:
                k = i
                break
        #  If we found no such k then the permutations are complete
        if k == -1:
            return
        # Find the largest l such that to_compute[k] < to_compute[l]
        l = k
        for i in reversed(range(k + 1, len(to_permute))):  # to_permute[k+1:]:
            if to_permute[l] < to_permute[i]:
                l = i
                break
        #  Swap elements k and l
        swap_elements(to_permute, k, l)
        #  Reverse the order of the elements K+1 to n
        to_permute = to_permute[:k + 1] + to_permute[:k:-1]


count = 0
result = ''
for perm in lexicographic_permutation_generator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    count += 1
    if count == 1000000:
        for d in perm:
            result += str(d)
        print(perm)
        break
print(result)