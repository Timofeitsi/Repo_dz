my_dict = {"Зима":[12, 1, 2], "Весна":[4, 5, 3], "Лето":[7, 8, 6], "Осень":[10, 11, 9]}
a = int(input("Введите порядковый номер месяца - "))
for key in my_dict:
    #if a in my_dict[key]:
    if my_dict[key].count(a):
        print('Это ', key)
        break
else:
    print("Так то в году 12 месяцев, подумайте еще раз")