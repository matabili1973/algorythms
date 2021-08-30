matr = []
for counter in range(5):
    matr.append([int(x) for x in input().split()])
    matr[-1].append(sum(matr[-1]))

print(*matr, sep = '\n')
