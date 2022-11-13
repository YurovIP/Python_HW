# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)


d = float(input('Точность округления = '))
k_round = 0
while d < 1:
    d *= 10
    k_round += 1

print(round(float(input('Округляемое число = ')), k_round))

# import math
# print(round(math.pi, k_round))