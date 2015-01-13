a = [0, 1, 5]

for i in a:
    try:
        b = a.index(a[i])
        print(b)
    except:
        continue
