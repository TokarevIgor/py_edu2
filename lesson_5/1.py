# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

count_comp = int(input('Введите кол-во предприятий: '))
comp_lst = []
comp_lst_small = []
comp_lst_big = []
avg_sum_all = 0
for comp_num in range(1, count_comp+1):
    comp_dict = {'name': input(f'Введите название {comp_num} компании: ')}
    val_dict = {}
    avg_sum = 0
    for i in range(1, 5):
        val_dict[i] = float(input(f'Введите прибыль {i} квартала: '))
        comp_dict['val'] = val_dict
        avg_sum += val_dict[i]
    comp_dict['avg_sum'] = avg_sum / 4
    avg_sum_all += comp_dict['avg_sum']
    comp_lst.append(comp_dict)

avg_sum_all = avg_sum_all / count_comp

for comp in comp_lst:
    if comp['avg_sum'] < avg_sum_all:
        comp_lst_small.append(comp['name'])
    else:
        comp_lst_big.append(comp['name'])

print(f"Средняя прибыль компаний составила: {avg_sum_all}")
print(f'{len(comp_lst_big)} компании чья прибыль выше средней:\n', *comp_lst_big)
print(f'{len(comp_lst_small)} компании чья прибыль ниже средней:\n', *comp_lst_small)
