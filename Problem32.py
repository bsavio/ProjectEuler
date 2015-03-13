"""
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from lib import lexicographic_permutations


def get_n_sums_of_x(n, x):
    if n < 0 or x < 0:
        raise ArithmeticError
    if n == 1:
        return [[x]]
    sums = []
    for d in range(0, x + 1):
        next_sums = get_n_sums_of_x(n - 1, x - d)
        for next_sum in next_sums:
            sums.append([d] + next_sum)
    return sums


def build_triplet(config, digits):
    if sum(config) != len(digits):
        raise ArithmeticError
    digit_index = 0
    triplet = []
    for c in config:
        term = 0
        for i in reversed(range(0, c)):
            term += digits[digit_index] * (10 ** i)
            digit_index += 1
        triplet.append(term)
    if len(triplet) != 3:
        raise Exception("Something went wrong")
    return triplet


def main():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    products = []
    product_configs = []
    three_tuple_sums_of_nine = get_n_sums_of_x(3, 9)  # get all 3-tuples that sum to 9 used for product configurations
    for three_tuple in three_tuple_sums_of_nine:  # for each configuration build each term to test
        if 0 not in three_tuple and three_tuple[2] >= max(three_tuple):  # skip configurations that are invalid
            triplet_to_test = build_triplet(three_tuple, [9, 9, 9, 9, 9, 9, 9, 9, 9])
            if len(str(triplet_to_test[0] * triplet_to_test[1])) > len(str(triplet_to_test[2])):
                product_configs.append(three_tuple)
    for perm in lexicographic_permutations(digits):
        for config in product_configs:
            product_triplet = build_triplet(config, perm)
            if product_triplet[2] in products:
                continue
            if product_triplet[0] * product_triplet[1] == product_triplet[2]:
                products.append(product_triplet[2])
    print(sum(products))


if __name__ == '__main__':
    main()