# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('N = '))

# lst_0 = []
# for i in range(2, n + 1):  # список простых чисел в диапазоне от 2 до n
#     if check_simple(i):
#         lst_0.append(i)
# print(lst_0)


def check_simple(x):  # проверка, является ли число простым
    if x > 1:
        for i in range(2, (x // 2) + 1):
            if (x % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def res(x, i):
    if i <= (x**(1/2)):
        if x % i == 0:
            if check_simple(i):
                lst.append(i)
                if check_simple(x // i):
                    return lst.append(x // i)
                else:
                    return res(x // (i), i)
        else:
            i += 1
            return res(x, i)


lst = []
if check_simple(n):
    print('Число', n, 'не имеет множителей, т.к. является простым числом')
else:
    res(n, 2)
    print('Список простых множителей числа', n, ':')
    print(lst)
