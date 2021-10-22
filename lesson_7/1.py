# №1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
import time


def sort_bubble_def(num_ls):
    n = 1
    while n < len(num_ls):
        for i in range(len(num_ls) - n):
            if num_ls[i] > num_ls[i + 1]:
                num_ls[i], num_ls[i + 1] = num_ls[i + 1], num_ls[i]
        n += 1


def my_sort_bubble_sort(num_ls, reverse=False):
    if reverse:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(num_ls)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if num_ls[i + left] > num_ls[i + right]:
                num_ls[i], num_ls[i + 1] = num_ls[i + 1], num_ls[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if num_ls[j - left] < num_ls[j - right]:
                num_ls[j], num_ls[j - 1] = num_ls[j - 1], num_ls[j]
        n += 1


ran_ls = [random.randint(-100, 100) for i in range(1000)]
ran_ls2 = ran_ls.copy()
print('Исходный:\n', ran_ls)

start_time = time.time()
sort_bubble_def(ran_ls)
print('Без доработок (без reverse)', (time.time() - start_time))
print(ran_ls)
# Без доработок 0.050829172134399414

start_time = time.time()
my_sort_bubble_sort(ran_ls2, True)
print('С доработкой (добавил reverse)', (time.time() - start_time))
print(ran_ls2)
# С доработкой 0.04645967483520508





