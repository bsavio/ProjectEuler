"""
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
  938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import csv


def calc_name_value(name):
    """
    Calculates name value
    :type name: str
    """
    name.upper()
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value


names = []
with open('Problem22_names.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        names += row
        break
name_scores = []
names.sort()
i = 0
while i < len(names):
    name_scores.append(calc_name_value(names[i]) * (i + 1))
    i += 1
print(sum(name_scores))