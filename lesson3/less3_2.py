"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать 
 параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def my_f1(**kwargs):
    global my_dict
    my_dict = kwargs
    return (kwargs)

name = input('введите имя пользователя - ')
surname = input('введите фамилию пользователя - ')
year = input('введите год рождения пользователя - ')
sity = input('введите город проживания пользователя - ')
email = input('введите адрес эл.почты пользователя - ')
phone = input('введите телефон пользователя - ')

print(f'Данные пользователя - {my_f1(Имя=name, Фамилия=surname, Год_рождения=year, Город_проживания=sity, Email=email, Телефон=phone)}\n')

for key in my_dict:
    print(f'{key}: {my_dict[key]}',end=", ")
    
    
#------------Второй вариант

def my_f2():
    name = input('введите имя пользователя - ')
    surname = input('введите фамилию пользователя - ')
    year = input('введите год рождения пользователя - ')
    sity = input('введите город проживания пользователя - ')
    email = input('введите адрес эл.почты пользователя - ')
    phone = input('введите телефон пользователя - ')
    my_dict = {"Имя": name, "Фамилия": surname, "Год_рождения": year, "Город_проживания": sity, "Email": email, "Телефон": phone}
    print('Данные пользователя:')
    for key in my_dict: print(f'{key}: {my_dict[key]}', end=", ")
    return
print(my_f2())