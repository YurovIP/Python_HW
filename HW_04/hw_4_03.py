# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

n = int(input('Размер числовой последовательности = '))
lst = []
lst_res = []

for i in range(n):
    lst.append(randint(0, 10))
print('Сформирован список элементов: ', lst)

for i in range(n):
    count = 0
    for j in range(n):
        if lst[i] == lst[j]:
            count += 1
    if count == 1:
        lst_res.append(lst[i])

print('Уникальные элементы сгенерированного списка:', lst_res)
