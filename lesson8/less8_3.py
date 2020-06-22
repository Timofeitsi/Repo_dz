class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
my_list = []
while True:
    string = input('Введите число (закончить q) - ')
    if string == 'q':
        break
    else:
        try:
            if string.isnumeric():
                string = int(string)
                my_list.append(string)
            else:
                raise OwnError('Введенные данные не числовые\nПожалуйста введите числовые данные')
        except OwnError as error:
            print(error)
            continue
print(my_list)