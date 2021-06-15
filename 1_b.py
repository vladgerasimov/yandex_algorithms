"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно,
выведите строку YES, иначе выведите строку NO.Ò
Треугольник — это три точки, не лежащие на одной прямой.
Формат ввода:
Вводятся три натуральных числа.
Формат вывода:
Выведите ответ на задачу.
"""

from sys import stdin

lengths = [int(stdin.readline()) for _ in range(3)]

if sum(lengths[:2]) > lengths[2] and sum(lengths[1:]) > lengths[0] and lengths[0] + lengths[2] > lengths[1]:
    print('YES')
else:
    print('NO')
