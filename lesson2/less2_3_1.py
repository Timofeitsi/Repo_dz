my_list = [[12, 1, 2], [4, 5, 3], [7, 8, 6], [10, 11, 9]]
a = int(input("Введите порядковый номер месяца - "))

for i in range(len(my_list)):
    if my_list[i].count(a):
        if i == 0:
            print("Зима")
            break
        elif i == 1:
            print("Весна")
            break
        elif i == 2:
            print("Лето")
            break
        elif i == 3:
            print("Осень")
            break
else:
    print("нет такого месяца")
