i = 0
sklad = []
while input("ввести товар - ") == "да":
    i+=1
    name = input("Наименование - ")
    price = input("Цена - ")
    coli = input("Количество - ")
    ed = input("Единица измерения - ")
    tovar = (i, {"название": name, "цена": int(price), "количество": int(coli), "ед.": ed,})
    sklad.append(tovar)
    
print("\n\nСклад:")
print('[')
for i in sklad:
    print(i)
print(']')
#print("\n\nСклад: \n", *sklad, sep='\n')

itog = {"название": [], "цена": [], "количество": [], "ед.": [],}

for i in range(len(sklad)):
    itog['название'].append(sklad[i][1].get('название'))
    itog['цена'].append(sklad[i][1].get('цена'))
    itog['количество'].append(sklad[i][1].get('количество'))
    itog['ед.'].append(sklad[i][1].get('ед.'))

itog['ед.'] = list(set(itog['ед.']))

print("\n\nОстатки на складе: \n")
print('{')
for key in itog.keys():
    print(key, '-->', itog[key])
print('}')