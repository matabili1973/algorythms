from random import randint as rint

mylist = [rint(-100, 101) for x in range(40)]
buffer = 0

for counter in range(-2, 0 - len(mylist) - 1, -1):
    for counter2 in range(-1, counter, -1):
        if mylist[counter] > mylist[counter2]:
            buffer = mylist[counter]
            mylist[counter] = mylist[counter2]
            mylist[counter2] = buffer

print(mylist[0], mylist[1])
