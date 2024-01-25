 
def f(fun):
    def g(n, *args):
        a = fun(*args)
        return ('false', 'true')[
            all(map(lambda x: a[x[0]][x[1]] == a[x[1]][x[0]], ((i, j) for i in range(n) for j in range(n))))]
 
    return g
 
@f
def h(*args):
    return args
 
 
n = int(input('Введите размерность матрицы: '))
arr =[list(map(int, input(f'Вводите в строчку через пробел, не более {n} значений: ').split())) for row in range(n)]
[print(*i) for i in arr]
 
print(h(n, *arr))