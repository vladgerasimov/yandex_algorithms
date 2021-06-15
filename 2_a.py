"""Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка
больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""

data = list(map(int, input().split()))


def is_ascending(data):
    prev = 0
    now = 1
    for _ in range(len(data) - 1):
        if data[prev] >= data[now]:
            return 'NO'
        prev = now
        now += 1
    return 'YES'


print(is_ascending(data))
