# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = input('Введите число: ')
str = '0123456789'
res = 0

for i in n:
    if i in str:
        x = int(i)
        res += x
print('Сумма цифр введенного числа = ', res)
