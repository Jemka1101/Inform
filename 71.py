def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Количество строк может быть только целым положительным')
 
 
# Тесты
n = int(input("Введите кол-во строк "))
read_last(n, 'article.txt')