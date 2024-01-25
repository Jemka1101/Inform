n = int(input())
res = []
for i in range(3,n+1):
    t = bin(i)[2:]
    if t == t[::-1]:
        d = 3
        while d*d <= i:
            if i%d == 0:
                break
            d += 2
        if d*d > i:
            res.append(i)
if len(res):
    print(res, '  ')
else:
    print('Таких чисел нет')