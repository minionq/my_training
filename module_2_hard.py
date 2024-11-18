result = ''
n = int(input('Введите число в левой ячейке: '))
while (n < 3) and (n > 20):
    print('Число введено неверно :(')
    n = int(input('Введите число в левой ячейке: '))
for i in range(1, n):
    for j in range(i + 1, n):
        if (n % (i + j)) == 0:
            result += str(i) + str(j)
print(result)