# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Введите координату точки по X, отличную от 0: '))
y = float(input('Введите координату точки по Y, отличную от 0: '))
if x == 0 or y == 0:
    print('Введены некорректные координаты!')
else:
    if x > 0 and y > 0:
        print('Заданная точка находится в I четверти плоскости координат')
    if x < 0 and y > 0:
        print('Заданная точка находится в II четверти плоскости координат')
    if x < 0 and y < 0:
        print('Заданная точка находится в III четверти плоскости координат')
    if x > 0 and y < 0:
        print('Заданная точка находится в IV четверти плоскости координат')
