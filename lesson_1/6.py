# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('Введите номер буквы в алфавите a-z (от 1 до 26):')
num = int(input())
char = chr(num + 64)
print(f'Буква "{char}"')
