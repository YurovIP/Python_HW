# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0


from random import randint

k = int(input('k = '))


def get_polinom(k):
    tmp = ''
    polinom = ''
    while k >= 0:
        n = randint(0, 101)
        if n != 0:
            if k > 1:
                n = str(n)
                k = str(k)
                tmp = (n + 'x^' + k + ' + ')
                polinom = polinom + tmp
            if k == 1:
                n = str(n)
                k = str(k)
                tmp = (n+'x' + ' + ')
                polinom = polinom + tmp
            if k == 0:
                n = str(n)
                k = str(k)
                tmp = (n + ' = 0')
                polinom = polinom + tmp
        k = int(k) - 1
    return polinom


polinom = get_polinom(k)
print(polinom)

with open('HomeWork\Less_04\get_polinom.txt', 'w') as data:
    data.write(polinom)
