"""
Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from timeit import default_timer
import csv


def get_words():
    words = []
    with open('Problem42_words.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            words += row
            break
    return words


def is_triangle_word(word):
    value = 0
    for letter in word:
        value += ord(letter) - 64
    value_to_test = (8*value + 1) ** 0.5
    return value_to_test - int(value_to_test) == 0


def main():
    words = get_words()
    count = 0
    for word in words:
        if is_triangle_word(word):
            count += 1
    print(count)
    return 0



if __name__ == '__main__':
    start = default_timer()
    main()
    print(u"Runtime: {0} ms".format((default_timer() - start) * 1000))