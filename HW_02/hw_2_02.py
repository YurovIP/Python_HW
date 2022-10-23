# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def f(x):
    if x == 1:
        return x
    else:
        return f(x-1) * x


n = int(input('N = '))
list = []
for e in range(1, n+1):
    list.append(f(e))
print(list)
