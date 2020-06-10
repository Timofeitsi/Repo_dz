'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
 были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

# задание 6
with open("text_6.txt", "r", encoding="utf-8") as less5_6:
    dict_5_6 = {}
    for line in less5_6:
        if (line.split(" ")[1]).count('-'):
            var1 = int((line.split(" ")[1]).replace('-', '0'))
        else:
            var1 = int((line.split(" ")[1]).replace('(л)', ''))
        if (line.split(" ")[2]).count('-'):
            var2 = int((line.split(" ")[2]).replace('-', '0'))
        else:
            var2 = int((line.split(" ")[2]).replace('(пр)', ''))
        if (line.split(" ")[3]).count('-'):
            var3 = int((line.split(" ")[3]).replace('-', '0'))
        else:
            var3 = int((line.split(" ")[3]).replace('(лаб)', ''))
        name = line.split(" ")[0]
        time = sum([var1, var2, var3])
        dict_5_6[name] = time
    print(dict_5_6)


# Задание 6 Вариант 2 (утром проснулся а он в голове)
with open("text_6.txt", "r", encoding="utf-8") as less5_6:
    dict_5_6 = {}
    dict_5_6_1 = {
        'Fizra': 'Физкультура',
        'Physics': 'Физика',
        'Literature': 'Литература',
        'History': 'История',
        'Math': 'Математика',
        'Informatics': 'Информатика',
        'Russian': 'Русский_язык'
    }
    for line in less5_6:
        temp_ = line.replace('(', ' (').replace(':', '') #отрываем числа от скобок, удалем двоеточия
        name = dict_5_6_1[temp_.split(" ")[0]]          # Заменяем название предмета из словаря если надо
    #   name = temp_.split(" ")[0]                      # Или не заменяем
        hours = sum([int(s) for s in temp_.split() if s.isdigit()]) # Добываем числа и суммируем
        dict_5_6[name] = hours # добавляем данные в словарь
    print(dict_5_6)

