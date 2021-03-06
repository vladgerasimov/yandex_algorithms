"""
Решите в целых числах уравнение:

sqrt(ax+b) = c,

a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.

Формат ввода
Вводятся три числа a, b и c по одному в строке.

Формат вывода Программа должна вывести все решения уравнения в порядке возрастания, либо NO SOLUTION (заглавными
буквами), если решений нет. Если решений бесконечно много, вывести MANY SOLUTIONS.
"""

a = int(input())
b = int(input())
c = int(input())

if c < 0 or (a == 0 and b != c ** 2):
    print('NO SOLUTION')
elif a == 0 and b == c ** 2:
    print('MANY SOLUTIONS')
else:
    x = (c ** 2 - b) / a
    if x == int(x):
        print(int(x))
    else:
        print('NO SOLUTION')
