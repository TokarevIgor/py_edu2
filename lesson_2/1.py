# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю
# о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def math_number(number1, number2, char_operation):

    if char_operation == '+':
        total = number1 + number2
    elif char_operation == '-':
        total = number1 - number2
    elif char_operation == '*':
        total = number1 * number2
    elif char_operation == '/':
        if number2 == 0:
            return 0, 'На ноль делить нельзя'
        else:
            total = number1 / number2
    else:
        return 0, 'Оператор не определен'

    return 1, f'{number1} {char_operation} {number2} = {total}'


run = True
while run:
    number1 = int(input('Введите 1 число: '))
    number2 = int(input('Введите 2 число: '))
    print('*** Помощь: 0 для выхода', '+ сложение', '- вычитание', '* умножение', '/ деление ***')
    repeat_input_char_operation = True
    while repeat_input_char_operation:
        char_operation = input('Введите символ операции: ')
        if char_operation == '0':
            run = False
            repeat_input_char_operation = False
            print("Программа завершена")
        else:
            result_math = math_number(number1, number2, char_operation)
            repeat_input_char_operation = result_math[0] == 0
            print(result_math[1])
