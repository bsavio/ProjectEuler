"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Parent/child relationships
By a result of Berggren (1934), all primitive Pythagorean triples can be generated from the (3, 4, 5) triangle by using the three linear transformations T1, T2, T3 below, where a, b, c are sides of a triple:

    new side a     new side b	   new side c
T1:	a − 2b + 2c    2a − b + 2c    2a − 2b + 3c
T2:	a + 2b + 2c    2a + b + 2c     2a + 2b + 3c
T3:	−a + 2b + 2c   −2a + b + 2c	   −2a + 2b + 3c



from lib import find_pythagorean_triplet

result = find_pythagorean_triplet(3, 4, 5, 1000)
print(result)
product = 1
for i in result:
    print(i)
    product *= i
print(product)
"""

from lib import primitive_pythagorean_triples

for triple in primitive_pythagorean_triples():
    triple.append(triple[0] + triple[1] + triple[2])
    if triple[3] >= 1000:
        break
    n = 1
    while triple[3] * n <= 1000:
        if triple[3] * n == 1000:
            print('*********************')
            print('FOUND IT!!')
            print(n)
            print(triple)
            triple[0] *= n
            triple[1] *= n
            triple[2] *= n
            triple[3] = triple[0] + triple[1] + triple[2]
            triple.append(triple[0] * triple[1] * triple[2])
            print(triple)
            break
        n += 1





