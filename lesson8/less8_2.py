class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    var_1 = input("Введите делимое, (q) для выхода - ")
    if var_1 == 'q':
        break
    try:
        var_1 = int(var_1)
    except ValueError:
        print('Введенные данные не числовые\nПожалуйста введите числовые данные')
        continue
    var_2 = input("Введите делитель, (q) для выхода - ")
    if var_2 == 'q':
        break
    try:
        var_2 = int(var_2)
        if var_2 == 0:
            raise OwnError("На ноль делить нельзя")
    except ValueError:
        print('Введенные данные не числовые\nПожалуйста введите числовые данные')
        continue
    except OwnError as error:
        print(error)
        continue
    print(f'Частное от {var_1} деленного на {var_2} равно {var_1 / var_2}')
