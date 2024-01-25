n = int(input("Введите верхний предел "))
s = 0
d = 1
if n > 100:
    print ("Ошибка")
else:
    for i in range(n):
        s += d ** 3
        d += 1
    print (s)