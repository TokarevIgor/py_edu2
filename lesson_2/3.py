# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = input('Введите число: ')

new_number = ''
for i in range(len(number)):
    i += 1
    new_number = new_number + number[i*-1]

print(int(new_number))
