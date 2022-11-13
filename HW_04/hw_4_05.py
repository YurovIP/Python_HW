# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


# читаем строку из файла и используем в качестве первого полинома
path = 'HomeWork\Less_04\get_polinom.txt'
data = open(path, 'r')
for line in data:
    polinom_1 = line
data.close()

print('Полином 1: ', polinom_1, '(импортированный из get_polinom.txt)')

# создаем новый полином и записываем его в файл
import hw_4_04

# читаем строку из файла и используем в качестве второго полинома
path = 'HomeWork\Less_04\get_polinom.txt'
data = open(path, 'r')
for line in data:
    polinom_2 = line
data.close()

print('Полином 2: ', polinom_2)

# перевод полинома в список элементов с коэффициентами
def get_list_from_polinom(a):
    left_part = a.replace(' = 0', '')
    lst = left_part.split(' + ')
    return lst

# вывод списков элементов с коэффициентами
lst_pol_1 = get_list_from_polinom(polinom_1)
# print(lst_pol_1)
lst_pol_2 = get_list_from_polinom(polinom_2)
# print(lst_pol_2)

# считаем максимальный коэффициент из входных данных
if (lst_pol_1[0][-1]) >= (lst_pol_2[0][-1]):
    k_max = int(lst_pol_1[0][-1])
else:
    k_max = int(lst_pol_2[0][-1])
# print('k_max =', k_max)

# создание списка коэффициентов
def get_lst_k(a):
    lst_k = []
    k = k_max
    find = ''
    while k >= 0:
        if k > 1:
            k = str(k)
            find = ('x^' + k)
            for i in range(len(a) + 1):
                if i < len(a):
                    if find in a[i]:
                        lst_k.append(a[i].replace(find, ''))
                        break
                else:
                    lst_k.append('0')
        if k == 1:
            for i in range(len(a) + 1):
                if i < len(a):
                    if 'x' in a[i]:
                        if '^' not in a[i]:
                            lst_k.append(a[i].replace('x', ''))
                            break
                else:
                    lst_k.append('0')
        if k == 0:
            for i in range(len(a) + 1):
                if i < len(a):
                    if 'x' not in a[i]:
                        lst_k.append(a[i])
                        break
                else:
                    lst_k.append('0')
        k = int(k)
        k -= 1
    return lst_k

k_polinom_a = get_lst_k(lst_pol_1)
k_polinom_b = get_lst_k(lst_pol_2)

# вывод списков с коэффициентами
# print(k_polinom_a)
# print(k_polinom_b)

# коэффициенты после операции сложения
lst_res = []
for i in range(len(k_polinom_a)):
    lst_res.append(int(k_polinom_a[i]) + int(k_polinom_b[i]))
# print('lst_res =', lst_res)

res_polinom = ''
k = k_max
tmp = ''
while k >= 0:
    n = lst_res[-(k + 1)]
    if n != 0:
        if k > 1:
            n = str(n)
            k = str(k)
            tmp = (n + 'x^' + k + ' + ')
            res_polinom = res_polinom + tmp
        if k == 1:
            n = str(n)
            k = str(k)
            tmp = (n+'x' + ' + ')
            res_polinom = res_polinom + tmp
        if k == 0:
            n = str(n)
            k = str(k)
            tmp = (n + ' = 0')
            res_polinom = res_polinom + tmp
    k = int(k) - 1
print('Сумма многочленов =',res_polinom)
