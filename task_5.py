"""

5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

"""

from random import randint

array = [randint(-20, 30) for n in range(10)]
print(f'Массив: {array}')

m = 0

for i in array:
    if array[m] > i:
        m = array.index(i)

if array[m] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {array[m]}.', f'Находится в массиве на позиции {m}')