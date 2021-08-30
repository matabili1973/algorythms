from random import randint

# Генератор списка со случайными целыми числами в заданных границах
mylist = [randint(-100, 100) for x in range(10)]

# Переменные для хранения значений и индексов минимального и максимального элементов
minval, maxval, minind, maxind = mylist[0], mylist[0], 0, 0

for counter, element in enumerate(mylist):
    if minval > element:
        minval = element
        minind = counter
    if maxval < element:
        maxval = element
        maxind = counter

print(*mylist)
mylist[minind] = maxval
mylist[maxind] = minval
print(*mylist)

