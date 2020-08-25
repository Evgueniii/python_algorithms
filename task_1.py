"""

5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

"""
# Вариант 1

import timeit
import cProfile
"""
def decode(i=32, counter=1):
    if i == 128:
        return
    print(f'{i} - {chr(i)}', end='')
    if counter % 10 == 0:
        print()
    i += 1
    counter += 1
    return decode(i, counter)
decode()

print(timeit.timeit('decode(i=32, counter=1)', number = 100, globals=globals())) # 0.052195515
print(timeit.timeit('decode(i=35, counter=1)', number = 100, globals=globals())) # 0.048974184000000004
print(timeit.timeit('decode(i=36, counter=1)', number = 100, globals=globals())) # 0.06134039599999999
print(timeit.timeit('decode(i=37, counter=1)', number = 100, globals=globals())) # 0.083644773
print(timeit.timeit('decode(i=38, counter=1)', number = 100, globals=globals())) # 0.07716932199999998

cProfile.run('decode(i=32, counter=1)')
#  97/1    0.000    0.000    0.001    0.001 task_1.py:22(decode)
cProfile.run('decode(i=35, counter=1)')
# 94/1    0.000    0.000    0.001    0.001 task_1.py:22(decode)
cProfile.run('decode(i=36, counter=1)')
#  93/1    0.000    0.000    0.001    0.001 task_1.py:22(decode)
cProfile.run('decode(i=37, counter=1)')
#  92/1    0.000    0.000    0.000    0.000 task_1.py:22(decode)
cProfile.run('decode(i=38, counter=1)')
# 91/1    0.000    0.000    0.000    0.000 task_1.py:22(decode)
"""
# Вариант 2

counter = 1
for i in range(32, 128):
    print(f'{i} - {chr(i)}', end='   |   ')
    if counter % 10 == 0:
        print()
    counter += 1

print(timeit.timeit('counter', number = 100, globals=globals())) # 3.55600000000178e-06
print(timeit.timeit('counter + 1', number = 100, globals=globals())) # 6.7160000000003606e-06
print(timeit.timeit('counter + 2', number = 100, globals=globals())) # 5.1359999999993355e-06
print(timeit.timeit('counter + 3', number = 100, globals=globals())) # 5.1359999999993355e-06
print(timeit.timeit('counter + 4', number = 100, globals=globals())) # 5.134999999999862e-06

cProfile.run('i')