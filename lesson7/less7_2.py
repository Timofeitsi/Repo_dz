from abc import ABC, abstractmethod

class Clothes(ABC):
    total_expense = []

    @staticmethod
    def total_exp():
        print(f'Общий расход ткани на все изделия, м - {round(sum(Clothes.total_expense), 2)}')
        #return round(sum(Clothes.total_expense), 2)

    @abstractmethod
    def expense_coat(self):
        return round(self.size / 6.5 + 0.5, 2)

    @abstractmethod
    def expense_costum(self):
        return round(self.height / 100 * 2 + 0.3, 2)

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        model_expense = super().expense_coat()
        to_sklag = super().total_expense
        to_sklag.append(model_expense)
    @property
    def size(self):
        return self.__size
    # сеттер для создания свойств
    @size.setter
    def size(self, size):
        if size < 44:
            self.__size = 44
        elif size > 58:
            self.__size = 58
        else:
            self.__size = size

    def expense_costum(self):
        pass
    def expense_coat(self):
        print(f'Расход ткани на изделие, м - {super().expense_coat()}')
        # return super().expense_coat()

class Costum(Clothes):
    def __init__(self, height):
        self.height = height
        model_expense = super().expense_costum()
        to_sklag = super().total_expense
        to_sklag.append(model_expense)
    @property
    def expense_costum(self):
        print(f'Расход ткани на изделие, м - {super().expense_costum()}')
        #return super().expense_costum()
    def expense_coat(self):
        pass

coat_1 = Coat(62)
coat_1.expense_coat()
Clothes.total_exp()

costum_1 = Costum(175)
costum_1.expense_costum
Clothes.total_exp()

costum_2 = Costum(150)
costum_2.expense_costum
Clothes.total_exp()
