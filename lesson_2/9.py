# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_input = input('Введите число, для выхода введите 0: \n')
max_num = 0
max_sum = 0
while num_input != '0':
    sum_num = 0
    for i in range(len(num_input)):
        sum_num += int(num_input[i * -1])
    if sum_num > max_sum:
        max_sum = sum_num
        max_num = num_input
    print(f'Максимальная сумма: {max_sum} , число: {max_num}')
    num_input = input('Введите число, для выхода введите 0: \n')
print('Программа завершена')
