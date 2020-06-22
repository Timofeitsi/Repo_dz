class MyDate():
    def __init__(self, datestr):
        try:
            day_num, month_num, year_num  = self.parse_datestr(datestr)
            if True:
                MyDate.verify(day_num, month_num, year_num)
                self.year_num = year_num
                self.month_num = month_num
                self.day_num = day_num
        except TypeError:
            self.year_num = 0
            self.month_num = 0
            self.day_num = 0
    day = 1
    mon = 1
    year = 1
    def __str__(self):
        if MyDate.day + MyDate.mon + MyDate.year != 3:
            prn_str = "Введите дату в верном формате"
        else:
            try:
                if self.year_num == 0 or self.day_num == 0 or self.month_num == 0:
                    prn_str = "Введите дату в верном формате"
                else:
                    prn_str = "Введена дата %02d-%02d-%02d" % (self.day_num, self.month_num, self.year_num)
            except Exception as err:
                prn_str = err
        return prn_str

    @classmethod
    def parse_datestr(cls, datestr):
        try:
            str_date = datestr.split('-')
            str_date = [int(str_date[0]), int(str_date[1]), int(str_date[2])]
            return str_date[0], str_date[1], str_date[2]
        except ValueError:
            print('Формат даты не соответствует шаблону')

    @staticmethod
    def verify(day_num, month_num, year_num):
        if not (day_num >= 1 and day_num <= 31):
            MyDate.day = 0
            print('День введен неверно')
            return True
        else:
            MyDate.day = 1
        if not (month_num >= 1 and month_num <= 12):
            MyDate.mon = 0
            print('Месяц введен неверно')
            return True
        else:
            MyDate.mon = 1
        if not (year_num >= 1000 and year_num <= 2999):
            print('Год введен неверно')
            MyDate.year = 0
            return True
        else:
            MyDate.year = 1


d = MyDate('3456-ЩЩ-ММММ')
print(d)
d = MyDate('31-13-2019')
print(d)
d = MyDate('41-13-1969')
print(d)
d = MyDate('05-11-1969')
print(d)
