s = input().split()

print(list(filter(lambda t: t.startswith('а') and t.endswith('я'), s)))