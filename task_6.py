"""
Задание 6.
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

"""
numb_letter = int(input('Введите номер буквы в алфавите:'))
if 0 < numb_letter < 27:
    print(f'Буква с этим номером - {chr(96 + numb_letter)}')
else:
    print(f'Буквы с номером {numb_letter} не существует')