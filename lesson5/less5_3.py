'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.
'''

less5_3 = open("text_3.txt", "r", encoding="utf-8")
list =[]
itog = 0
for line in less5_3:
    summa = float(line.split(" ")[1].replace('\n', ''))
    name = (line.split(" ")[0])
    data = {name: summa}
    list.append(data)
    itog = itog + summa
    if summa < 20000.0:
        print(f'{name} имеет оклад менее 20000')
print(list)
print(f'{itog/len(list)} тугриков средняя величина дохода')
less5_3.close()
