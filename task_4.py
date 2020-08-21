"""

4. Определить, какое число в массиве встречается чаще всего.

"""

from random import randint

array = [randint(0, 50) for _ in range(10)]
print(f'Массив: {array}')

max_index = 0
for i in array:
    if array.count(max_index) < array.count(i):
        max_index = array.index(i)

print(f'Число {array[max_index]}, встречается {array.count(max_index)} раз')