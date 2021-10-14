# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках домашнего задания первых трех уроков.

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import cProfile

print('1 метод')


def my_func():
    import random

    random_list = [random.randint(0, 100) for i in range(10)]
    print(*random_list)

    min_el = random_list[0]
    max_el = random_list[1]

    min_idx = 0
    max_idx = 1
    for i, item in enumerate(random_list):
        if item <= min_el:
            min_el = item
            min_idx = i
        elif item >= max_el:
            max_el = item
            max_idx = i

    random_list[min_idx] = max_el
    random_list[max_idx] = min_el

    print('Результат:\n', *random_list)


cProfile.run('my_func()')
# 1182 function calls (1144 primitive calls) in 0.008 seconds

print('2 метод')


def my_func1():
    import random

    random_list = [random.randint(0, 100) for i in range(10)]
    print(*random_list)

    min_el = random_list[0]
    max_el = random_list[1]

    min_idx = 0
    max_idx = 1
    for i, item in enumerate(random_list):
        if item <= min_el:
            min_el = item
            min_idx = i
        elif item >= max_el:
            max_el = item
            max_idx = i

    random_list[min_idx] = max_el
    random_list[max_idx] = min_el

    print('Результат:\n', *random_list)


cProfile.run('my_func1()')

