# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('N = '))
lst = []
for i in range(1, n+1):
    lst.append((1 + 1 / i) ** i)
# print(lst)

sum = 0
for i in range(len(lst)):
    sum = sum+lst[i]
print(sum)
