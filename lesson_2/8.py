# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

str_num_input = input('Введите последовательность чисел разделяя пробелом, которое хотите подсчитать: \n')
# наверное чуть вперед забегаю, но ведь удобно )
lst_num = [int(num) for num in str_num_input.split(' ')]
find_num = int(input('Введите число, которое нужно посчитать: \n'))
print(f'{find_num} встречается: {lst_num.count(find_num)}')
