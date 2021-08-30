mdict = {2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
for counter in range(2, 100):
    for divider in mdict.keys():
        if not counter % divider:
            mdict[divider] += 1

print(*mdict.items())
