'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

with open("text_4.txt", "r", encoding="utf-8") as less5_4:
    less5_4_1 = open("text_4_1.txt", "w+", encoding="utf-8")
    dict_5_4 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    list = []
    for line in less5_4:
        list = line.split(" ")
        name = line.split(" ")[0]
        list[0] = dict_5_4[name]
        print(f"{list[0]} {list[1]} {list[2]}", file=less5_4_1, end="")
    less5_4_1.close()

# Задание 4 вар 2

from googletrans import Translator
translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as less5_4:
    less5_4_1 = open("text_4_1.txt", "w+", encoding="utf-8")
    list = []
    for line in less5_4:
        list = line.split(" ")
        name = translator.translate(line.split(" ")[0], dest='ru').text.title()
        print(name)
        print(f"{name} {list[1]} {list[2]}", file=less5_4_1, end="")
    less5_4_1.close()
