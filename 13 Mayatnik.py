from math import pi, sqrt
g = 9.81
L = float(input("Введите длинну: "))
print ("Период = ", str( round(2 * pi * sqrt(L / g), 2)))