"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

scr_name, time_in_hours, tarif, bonus = argv
print(int(time_in_hours) * int(tarif) + int(bonus))
'''
try:
time, stavka, premia = map(int, argv[1:])
print(f'salary - {time*stavka + premia})
except:
ValueError
'''