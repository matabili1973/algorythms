from random import randint

mylist = [randint(-100, 101) for x in range(40)]
mynum = 0
myind = 0

for counter, element in enumerate(mylist):
    if not mynum:
        if element < 0:
            mynum = element
            myind = counter
    else:
        if element < 0 and abs(mynum) > abs(element):
            mynum = element
            myind = counter

print(f'Наибольший отрицательный элемент массива находится на {myind} месте, и равен {mynum}')
