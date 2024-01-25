import math
def corner(x,y):
    n = float(math.degrees(math.atan(y/x)))
    return n

x = int(input())
y = int(input())
z = float(corner(x,y))
for i in range (2):
    x = int(input())
    y = int(input())
    k = corner(x,y)
    if k < z:
        z = k
print (z)
