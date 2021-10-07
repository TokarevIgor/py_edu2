# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

final_dict = dict.fromkeys(range(2, 10), 0)
for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            final_dict[i] += 1

for key in final_dict:
    print(f'{key} кратны {final_dict[key]} чисел')
