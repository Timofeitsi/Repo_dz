"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_f1(*args):
    args = list(args)
    args.remove(min(args))
    return sum(args)

while True:
    try:
        var_1 = int(input("Введите число: "))
        break
    except ValueError:
        print("Введенные данные не числовые, попробуйте еще раз")
while True:
    try:
        var_2 = int(input("Введите число: "))
        break
    except ValueError:
        print("Введенные данные не числовые, попробуйте еще раз")
while True:
    try:
        var_3 = int(input("Введите число: "))
        break
    except ValueError:
        print("Введенные данные не числовые, попробуйте еще раз")

print(f'Сумма двух наибольших аргументов - {my_f1(var_1, var_2, var_3)}')

#--------------Второй вариант

def my_f2():
    arg = []
    i = 1
    for i in range(3):
        try:
            var = int(input("Введите число: "))
        except ValueError:
            print("Введенные данные не числовые, попробуйте еще раз")
        arg.append(var)
    arg.remove(min(arg))
    return sum(arg)

print(f'Сумма двух наибольших аргументов - {my_f2()}')

#----------------Третий вариант

def my_f3():
    
    while True:
        try:
            var_1 = int(input("Введите число: "))
            break
        except ValueError:
            print("Введенные данные не числовые, попробуйте еще раз")
    while True:
        try:
            var_2 = int(input("Введите число: "))
            break
        except ValueError:
            print("Введенные данные не числовые, попробуйте еще раз")
    while True:
        try:
            var_3 = int(input("Введите число: "))
            break
        except ValueError:
            print("Введенные данные не числовые, попробуйте еще раз")

    args = [var_1, var_2, var_3]
    args.remove(min(args))
    return sum(args)


print(f'Сумма двух наибольших аргументов - {my_f3()}')


