# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import random
import sys

""" Версия """


# print(sys.version)
# 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


def lesson_3_task_5():
    # Задание
    # В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

    ran_lst = [random.randint(-15, 10) for i in range(5)]

    min_num = ran_lst[0]
    min_idx = 0

    for i, item in enumerate(ran_lst):
        if item < min_num and item < 0:
            min_num = item
            min_idx = i

    return locals()


"""
lesson 3 task 5
 type = <class 'dict'>, size = 232, object = {'ran_lst': [7, -15, 3, -15, -9], 'min_num': -15, 'min_idx': 1, 'i': 4, 'item': -9}
	 type = <class 'tuple'>, size = 56, object = ('ran_lst', [7, -15, 3, -15, -9])
		 type = <class 'str'>, size = 56, object = ran_lst
		 type = <class 'list'>, size = 120, object = [7, -15, 3, -15, -9]
			 type = <class 'int'>, size = 28, object = 7
			 type = <class 'int'>, size = 28, object = -15
			 type = <class 'int'>, size = 28, object = 3
			 type = <class 'int'>, size = 28, object = -15
			 type = <class 'int'>, size = 28, object = -9
	 type = <class 'tuple'>, size = 56, object = ('min_num', -15)
		 type = <class 'str'>, size = 56, object = min_num
		 type = <class 'int'>, size = 28, object = -15
	 type = <class 'tuple'>, size = 56, object = ('min_idx', 1)
		 type = <class 'str'>, size = 56, object = min_idx
		 type = <class 'int'>, size = 28, object = 1
	 type = <class 'tuple'>, size = 56, object = ('i', 4)
		 type = <class 'str'>, size = 50, object = i
		 type = <class 'int'>, size = 28, object = 4
	 type = <class 'tuple'>, size = 56, object = ('item', -9)
		 type = <class 'str'>, size = 53, object = item
		 type = <class 'int'>, size = 28, object = -9
		 """


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
def lesson_3_task_1():
    final_dict = dict.fromkeys(range(2, 10), 0)
    for num in range(2, 100):
        for i in range(2, 10):
            if num % i == 0:
                final_dict[i] += 1

    return locals()


""" 
lesson 3 task 1
 type = <class 'dict'>, size = 232, object = {'final_dict': {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}, 'num': 99, 'i': 9}
	 type = <class 'tuple'>, size = 56, object = ('final_dict', {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11})
		 type = <class 'str'>, size = 59, object = final_dict
		 type = <class 'dict'>, size = 360, object = {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
			 type = <class 'tuple'>, size = 56, object = (2, 49)
				 type = <class 'int'>, size = 28, object = 2
				 type = <class 'int'>, size = 28, object = 49
			 type = <class 'tuple'>, size = 56, object = (3, 33)
				 type = <class 'int'>, size = 28, object = 3
				 type = <class 'int'>, size = 28, object = 33
			 type = <class 'tuple'>, size = 56, object = (4, 24)
				 type = <class 'int'>, size = 28, object = 4
				 type = <class 'int'>, size = 28, object = 24
			 type = <class 'tuple'>, size = 56, object = (5, 19)
				 type = <class 'int'>, size = 28, object = 5
				 type = <class 'int'>, size = 28, object = 19
			 type = <class 'tuple'>, size = 56, object = (6, 16)
				 type = <class 'int'>, size = 28, object = 6
				 type = <class 'int'>, size = 28, object = 16
			 type = <class 'tuple'>, size = 56, object = (7, 14)
				 type = <class 'int'>, size = 28, object = 7
				 type = <class 'int'>, size = 28, object = 14
			 type = <class 'tuple'>, size = 56, object = (8, 12)
				 type = <class 'int'>, size = 28, object = 8
				 type = <class 'int'>, size = 28, object = 12
			 type = <class 'tuple'>, size = 56, object = (9, 11)
				 type = <class 'int'>, size = 28, object = 9
				 type = <class 'int'>, size = 28, object = 11
	 type = <class 'tuple'>, size = 56, object = ('num', 99)
		 type = <class 'str'>, size = 52, object = num
		 type = <class 'int'>, size = 28, object = 99
	 type = <class 'tuple'>, size = 56, object = ('i', 9)
		 type = <class 'str'>, size = 50, object = i
		 type = <class 'int'>, size = 28, object = 9
"""

print('lesson 3 task 5')
show_size(lesson_3_task_5())
print('lesson 3 task 1')
show_size(lesson_3_task_1())
