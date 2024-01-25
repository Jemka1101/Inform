from operator import ne
from functools import partial
 
 
def is_magic(mat):
    gauge = sum(next(iter(mat)))
    return  not any(map(partial(ne, gauge), map(sum, mat)))     \
        and not any(map(partial(ne, gauge), map(sum, zip(*mat))))

n = int(input('Введите размерность матрицы: '))
arr =[list(map(int, input(f'Вводите в строчку через пробел, не более {n} значений: ').split())) for row in range(n)]
[print(*i) for i in arr]

print(is_magic(arr))