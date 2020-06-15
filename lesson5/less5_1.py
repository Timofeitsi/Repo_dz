'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
'''

with open("less5hw1.txt", "w+", encoding="utf-8") as less5_1:
    string = None
    while  string != "":
        string = input('Введите данные - ')
        try:
            print(string)
            less5_1.write(f"{string}\n")
        except:
            break
    less5_1.seek(0)  # Прыжок в начало файла или нужную позицию
    for i in less5_1:
        print(i, end="")

