import timeit


def cardinality_check1(numbers_dict):
    for n in range(2, 200):
        for k, i in numbers_dict.items():
            if n % k == 0:
                i += 1
                numbers_dict[k] = i


numbers_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

time1 = timeit.timeit(f'cardinality_check1({numbers_dict})',
                      setup='from __main__ import cardinality_check1',
                      number=1)


def cardinality_check2():
    final_dict = dict.fromkeys(range(2, 10), 0)
    for num in range(2, 200):
        for i in range(2, 10):
            if num % i == 0:
                final_dict[i] += 1


time2 = timeit.timeit(f'cardinality_check2()',
                      setup='from __main__ import cardinality_check2',
                      number=1)

print('Первый вариант: {}'.format(time1))
print('Второй вариант: {}'.format(time2))