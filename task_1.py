"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1jV3ts5fBoM3e9hsxVPMJggKvx_KO19pd/view?usp=sharing - ссылка на диаграммы.
"""
number = int(input('Введите положительное трехзначное число: '))
if number > 0:
    a = number // 100
    b = (number // 10) % 10
    c = number % 10
    print(f'Сумма цифр {number} = {a + b + c}')
    print(f'Произведение цифр {number} = {a * b * c}')
else:
    print(f'Вы ввели число не удовлетворяющее условию и будете прокляты!!!')

