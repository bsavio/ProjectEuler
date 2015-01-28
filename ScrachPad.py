to_permute = [0, 2, 1, 3, 4]
k = 1
l = to_permute[:k+1] + to_permute[:k:-1]
for i in reversed(range(0, len(to_permute) - 1)):
    print(i)

print(l)
