"""
Задание 5.
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

"""

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')

number_1 = ord(letter_1) - 96
number_2 = ord(letter_2) - 96

print(f'Буква {letter_1} стоит на {number_1} месте')

print(f'Буква {letter_2} стоит на {number_2} месте')

sum_letter = number_2 - number_1 - 1 if number_2 > number_1 else number_1 - number_2 - 1

print(f'Между буквами {letter_1} и {letter_2}: {sum_letter} букв(ы)')