"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""


def num_to_word(n):
    one_to_nineteen_words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                             'nineteen']
    tens_place_words = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    thousands = int(n/1000) % 10
    hundreds = int(n/100) % 10
    tens = int(n/10) % 10
    ones = n % 10
    result_word = ''
    if thousands > 0:
        result_word += one_to_nineteen_words[thousands] + 'thousand'
    if hundreds > 0:
        result_word += one_to_nineteen_words[hundreds] + 'hundred'
        if tens > 0 or ones > 0:
            result_word += 'and'
    if tens > 1:
        result_word += tens_place_words[tens] + one_to_nineteen_words[ones]
    else:
        result_word += one_to_nineteen_words[(10 * tens) + ones]
    return result_word


result = 0
for i in range(1, 1001):
    result += len(num_to_word(i))
print(result)