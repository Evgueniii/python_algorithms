"""
Задание 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
first_number = 5
second_number = 6
bin_and = first_number & second_number
print(f'Побитовый И {first_number} и {second_number} = {bin_and}')
bin_or = first_number | second_number
print(f'Побитовый ИЛИ {first_number} и {second_number} = {bin_and}')
bit_shift_right = first_number >> 2
print(f'Побитовый сдвиг вправо {first_number} = {bit_shift_right}')
bit_shift_left = first_number << 2
print(f'Побитовый сдвиг влево {first_number} = {bit_shift_left}')