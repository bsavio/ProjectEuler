"""
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from timeit import default_timer


def main():
    perimeters = [0] * 1001
    for a in range(1, 999):
        for b in range(1, 999 - a):
            c = (a ** 2 + b ** 2) ** .5
            if c == int(c) and a + b + c <= 1000:
                perimeters[int(a + b + c)] += 1
    print(perimeters.index(max(perimeters)))
    return 0


if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))