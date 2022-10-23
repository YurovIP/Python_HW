# Реализуйте алгоритм перемешивания списка.

from random import randint


n = int(input('N = '))
lst = []
for i in range(1, n+1):
    lst.append(randint(-(n*n), n*n))
print('Сгенерирован список:\n', lst)

get_lst = []
for i in range(len(lst)):
    x = randint(0, len(lst)-1)
    get_lst.append(lst[x])
    lst.pop(x)

print('Получен список:\n', get_lst)
