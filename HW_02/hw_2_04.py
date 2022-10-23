# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


n = int(input('N = '))
lst = []

for i in range(1, n+1):
    lst.append(randint(-n, n))
print('Сгенерирован список:\n', lst)

data = open('HomeWork\Less_02\hw_file.txt', 'r')
lst_data = []
for line in data:
    lst_data.append(int(line))
data.close()
print('Высчитываем произведение элементов с индексами:\n', lst_data)

res = 1
for i in lst_data:
    if i <= len(lst):
        res = (res*lst[i])
    else:
        print('Сгенерированный список не содержит элемента с искомым индексом')
        exit()

print('Произведение = ', res)
