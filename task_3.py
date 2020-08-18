"""

3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

"""

number = int(input('Введите число, которое впоследстии перевернется: '))
reversed_number = ''

while not number == 0:
    tmp_num = number % 10
    reversed_number += str(tmp_num)
    number = number // 10

print(f'Перевернутое число: {reversed_number}')