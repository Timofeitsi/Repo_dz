"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо 
получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()
"""
new_list5 = [el for el in range(100, 1001) if el % 2 == 0]
result = 1
for i in range(0, len(new_list5)):
    result *= int(new_list5[i])
print(result)

from functools import reduce
def reducer_f(el_prev, el):
    return el_prev * el

result = reduce(reducer_f, [el for el in range(100, 1001) if el % 2 == 0])
print(result)

result1 = reduce(lambda a, x : a * x, [el for el in range(100, 1001) if el % 2 == 0])
print(result1)
