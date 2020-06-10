'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from itertools import count
from random import randint
with open("text_5.txt", "w", encoding="utf-8") as less5_5:
    for el in count(randint(20, 100), 1): 
        if el > 100:
            break
        else:
            str = int(randint(1, 100))
            print(str, end=' ', file=less5_5)
with open("text_5.txt", "r", encoding="utf-8") as less5_5:
    for line in less5_5:
        summa = sum([int(s) for s in line.split() if s.isdigit()])
        print(summa)
