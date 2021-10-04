# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

first_char = 32
end_char = 127
lst = []
count = 0
for i in range(first_char, end_char + 1):
    lst.append(f'{i} {chr(i)}')
    count += 1
    if count == 10 or i == end_char:
        print(' '.join(lst))
        lst.clear()
        count = 0
