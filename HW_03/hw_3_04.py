# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Задайте число: '))


def f_bin(n):
    if n != 0:
        x = int(n % 2)
        n = int(n/2)
        f_bin(n)
        print(x, end='')
        return x
    else:
        return 0


f_bin(n)
