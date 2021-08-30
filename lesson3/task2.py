print('Введите числа, входящие в массив, одной строкой через пробел:\n')
list1 = [int(x) for x in input().split()]
list2 = []

# Раньше я всегда делал это с помощью функции range(len(list1))
for counter, element in enumerate(list1):
    if not element % 2:
        list2.append(counter)

print(*list2)
