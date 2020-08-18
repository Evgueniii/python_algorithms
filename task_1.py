"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю
о невозможности деления на ноль, если он ввел его в качестве делителя.

https://drive.google.com/file/d/14jeoCYxEt8MMA7zf3xuiythLeETuDOkn/view?usp=sharing - ссылка на диаграммы.

"""

while True:
    operation_sign = input('Введите знак операции ("+", "-", "*", "/") или "0" для выхода из программы: ')
    if not operation_sign == '0' and not operation_sign.isdigit():
        number_1 = input('Введите первое число: ')
        number_2 = input('Введите первое число: ')
        if number_1.isdigit() and number_2.isdigit():
            if operation_sign == '+':
                result = int(number_1) + int(number_2)
                print(f'Результат: {number_1} + {number_2} = {result}')
            elif operation_sign == '-':
                result = int(number_1) - int(number_2)
                print(f'Результат: {number_1} - {number_2} = {result}')
            elif operation_sign == '*':
                result = int(number_1) * int(number_2)
                print(f'Результат: {number_1} * {number_2} = {result}')
            elif operation_sign == '/':
                if not number_2 == '0':
                    result = int(number_1) / int(number_2)
                    print(f'Результат: {number_1} / {number_2} = {result}')
                else:
                    print('Делить на ноль не стоит, попробуй еще раз!')
        else:
            print('Ну что же ты такой не внимательный, попробуй еще раз!')
    elif operation_sign == '0':
        break
    else:
        print('Ну что же ты такой не внимательный, попробуй еще раз!')
    continue