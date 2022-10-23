# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('x = ')
y = input('y = ')
z = input('z = ')
print((not (x or y or z)) == ((not x) and (not y) and (not z)))
