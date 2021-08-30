from random import randint

mydict = {}
mylist = [randint(-10, 11) for x in range(40)]

for element in mylist:
    if element not in mydict.keys():
        mydict[element] = 1
    else:
        mydict[element] += 1

reskey, resnum = 0, 0
for key, val in mydict.items():
    if val > resnum:
        reskey = key
        resnum = val

print(f'Чаще всего встречается число {reskey}, которое повторяется {resnum} раз')
