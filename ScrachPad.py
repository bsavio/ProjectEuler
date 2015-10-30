import lib

for x in lib.pentagonal_numbers():
    print(x)
    print(lib.is_pentagonal(x))
    if x >= 145:
        break