arr =[list(map(int, input(f'Вводите в строчку через пробел, не более {3} значений: ').split())) for row in range(3)]
[print(*i) for i in arr]
max = arr [0] [2]
for i in range(3):
    for j in range (3):
        if max < arr [i] [2]:
            max = arr [i] [2]
print('Максимум третьего столбца ', max)
max = arr [1] [0]
for i in range(3):
    for j in range (3):
        if max < arr [1] [j]:
            max = arr [1] [j]
print("Максимум второй строки ", max)