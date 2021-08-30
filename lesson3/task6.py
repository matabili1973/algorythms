from random import randint as rint

def getmin(a):
    mynum = a[0]
    for element in a:
        if element < mynum:
            mynum = element
    return mynum

def getmax(a):
    mynum = a[0]
    for element in a:
        if element > mynum:
            mynum = element
    return mynum



mylist = [rint(-100, 101) for x in range(40)]
minnum = getmin(mylist)
maxnum = getmax(mylist)
res = 0

for counter in mylist:
    if minnum < counter < maxnum:
        res += counter

print(f'Сумма всех элементов массива, кроме наименьшего и наибольшего, равна {res}')
