i = 12345
i_length = len(str(i))
n = i
for x in range(i_length):
    print(n)
    n = (n % 10 * 10 ** (i_length-1)) + (n // 10)
