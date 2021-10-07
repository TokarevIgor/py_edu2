# Определить, какое число в массиве встречается чаще всего.

import random

ran_lst = [random.randint(1, 3) for i in range(15)]
dict_repeat = dict.fromkeys(ran_lst, 0)
for key in dict_repeat:
    dict_repeat[key] = ran_lst.count(key)

max_key = 0
max_count = 0

for key in dict_repeat:
    count = dict_repeat[key]
    if max_key == 0 or count > max_count:
        max_key = key
        max_count = count

print(f'{ran_lst}\n{dict_repeat}')
print(f'Максимально встречается: {max_key} = {max_count} раз')
