"""

1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""

from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_sort_1(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False
        if flag == True:
            break
    return array

def bubble_sort_2(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array

numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort_1(numbers))

time1 = timeit(f'bubble_sort_1({numbers})',
              setup='from __main__ import bubble_sort_1',
              number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_2({numbers})',
              setup='from __main__ import bubble_sort_2',
              number=NUMBER_EXECUTIONS)
print(time1)
print(time2)