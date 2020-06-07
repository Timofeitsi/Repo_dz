"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
def gen_list(our_list):
    temp_list = []
    for i in range(len(our_list)):
        try:
            if our_list[i] >= our_list[(i + 1)]:
                continue
            temp_list.append(our_list[(i + 1)])
        except IndexError:
            break
    return temp_list

my_list2 =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 152]

new_list2_1 = gen_list(my_list2)
print(new_list2_1)

new_list2_2 = [my_list2[el] for el in range(1, len(my_list2)) if my_list2[el] > my_list2[(el - 1)]]
print(new_list2_2)
