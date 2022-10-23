# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint


n = int(input('Размер генерируемого списка: '))

lst = []
for i in range(1, n+1):
    lst.append(randint(-10, 10))
print('Сгенерирован список\n', lst)

lst_res = []
n_res = int(n/2 if n % 2 == 0 else (n//2+1))
for i in range(0, n_res):
    lst_res.append(lst[i] * lst[-i-1])
print(lst_res)
