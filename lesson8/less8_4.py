class Stock_org:

    Stock_org_total = {} # Склад основной
    count = 0 # Выдача инвентарных номер -  ов
    filial1 = {} # Филиал
    basket = {} #корзина удалений

    @staticmethod
    def fil_to_skl(): # перемещение филиал склад
        print('перемещение филиал склад')
        i = int(input('введите инвентарный номер -  '))
        Stock_org.Stock_org_total[i] = Stock_org.filial1[i]
        del Stock_org.filial1[i]

    @staticmethod
    def skl_to_fil(): # перемещение склад филиал
        print('перемещение склад филиал')
        i = int(input('введите инвентарный номер -  '))
        Stock_org.filial1[i] = Stock_org.Stock_org_total[i]
        del Stock_org.Stock_org_total[i]

    @staticmethod
    def skl_to_basket(): # удаление в корзину
        print('удаление в корзину')
        i = int(input('введите инвентарный номер -  '))
        Stock_org.basket[i] = Stock_org.Stock_org_total[2]
        del Stock_org.Stock_org_total[i]

    @staticmethod
    def clear_basket():  # очистка корзины
        print('очистка корзины')
        Stock_org.basket = {}

class Orgtechniks:
    def __init__(self, techniks_name, techniks_mark):
        self.techniks_name = techniks_name
        self.techniks_mark = techniks_mark

    count = 0

class Printers(Orgtechniks):
    def __init__(self, techniks_name, techniks_mark, techniks_type):
        self.techniks_name = techniks_name
        self.techniks_mark = techniks_mark
        self.techniks_type = techniks_type
        Orgtechniks.count += 1
        Stock_org.count += 1
        (Stock_org.Stock_org_total)[Stock_org.count] = {'printers': [self.techniks_name, self.techniks_mark, self.techniks_type]}

class Scanner(Orgtechniks):
    def __init__(self, techniks_name, techniks_mark, techniks_type):
        self.techniks_name = techniks_name
        self.techniks_mark = techniks_mark
        self.techniks_type = techniks_type
        Orgtechniks.count += 1
        Stock_org.count += 1
        (Stock_org.Stock_org_total)[Stock_org.count] = {'scanner': [self.techniks_name, self.techniks_mark, self.techniks_type]}

class Computers(Orgtechniks):
    def __init__(self, techniks_name, techniks_mark, techniks_type):
        self.techniks_name = techniks_name
        self.techniks_mark = techniks_mark
        self.techniks_type = techniks_type
        Orgtechniks.count += 1
        Stock_org.count += 1
        (Stock_org.Stock_org_total)[Stock_org.count] = {'computer': [self.techniks_name, self.techniks_mark, self.techniks_type]}


printer = Printers('Sony', 'lx-200', 'matrix')
scanner = Scanner('Panasonic', '325', 'home')
printer2 = Printers('Sony', 'lx-200', 'matrix')
printer3 = Printers('Sony', 'lx-200', 'matrix')


d = (Stock_org.Stock_org_total)
print()
# список принтеров на складе
for key, value in d.items():

    a = value
    for key, value in a.items():
        if key == 'printers':
            print(value)


print(f'количество принтеров на складе = {value}')
print()

print(Stock_org.skl_to_fil())
print(f'филиал -- {Stock_org.filial1}')
print(Stock_org.Stock_org_total)
print(f'корзина -- {Stock_org.basket}')
print()

print(Stock_org.fil_to_skl())
print(f'филиал -- {Stock_org.filial1}')
print(Stock_org.Stock_org_total)
print(f'корзина -- {Stock_org.basket}')
print()

print(Stock_org.skl_to_basket())
print(f'филиал -- {Stock_org.filial1}')
print(Stock_org.Stock_org_total)
print(f'корзина -- {Stock_org.basket}')
print()

(Stock_org.clear_basket())
print(f'филиал -- {Stock_org.filial1}')
print(Stock_org.Stock_org_total)
print(f'корзина -- {Stock_org.basket}')
print()

#вывод сортированного словаря
#list_keys = list(d.keys())
#>>> list_keys.sort()
#>>> for i in list_keys:
#...     print(i, ':', d[i])