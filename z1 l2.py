# -*- coding: cp1251 -*-  <-- Добавь эту строку в начало!
from math import sqrt

x = float(input('Введите значение x='))

if x < -4:
    y = -1
elif x >= -4 and x < -2:
    y = x + 3
elif x >= -2 and x < 4:
    y = -x / 2
elif x >= 4 and x < 6:
    y = -2
elif x >= 6 and x < 10:
    y = -2 + sqrt(4 - (x - 8)**2)
else:  # x >= 10
    y = -2

print("X={0:.2f}    Y={1:.2f}".format(x, y))