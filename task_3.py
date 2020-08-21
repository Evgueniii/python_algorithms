"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

from random import randint

array = [randint(-100, 1000) for _ in range(10)]
print(f'Старый массив: {array}')

n_max = 0
n_min = 0

for i in array:
    if i > n_max:
        n_max = i
    elif i < n_min:
        n_min = i

array[array.index(n_max)], array[array.index(n_min)] = array[array.index(n_min)], array[array.index(n_max)]

print(f'Новый массив:  {array}')
print(f'Поменяли местами числа {n_max} и {n_min}')
