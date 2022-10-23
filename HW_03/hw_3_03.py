# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

import random

n = int(input('Размер генерируемого списка = '))

lst = []
for i in range(1, n+1):
    lst.append(round(random.uniform(-10, 10), 2))

lst_min = 10
lst_max = 0
for i in range(len(lst)):
    x = abs(round(lst[i]-int(lst[i]/1), 2))
    if x > lst_max:
        lst_max = x
    if x < lst_min:
        lst_min = x

# print(lst)
# # print('min = ', lst_min, '; max = ', lst_max)
# print('Разница между максимальным и минимальным значением дробной части элементов = ',round(lst_max - lst_min, 2))

print(lst, '=>', round(lst_max - lst_min, 2))