s = input()
lst = list(s)
count = tmp = 0
for i in range(len(lst)):
    if lst[i] == 'н':
        tmp += 1
    if lst[i] != 'н' or i == len(lst) - 1:
        count = max(count, tmp)
        tmp = 0
print (count)
str_replaced = s.replace('!','.')
print(str_replaced)