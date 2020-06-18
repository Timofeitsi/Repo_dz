from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        self.size = size
        self.height = height

    @abstractmethod
    def expense_coat(self):
        return round(self.size / 6.5 + 0.5, 2)

    @abstractmethod
    def expense_costum(self):
        return round(self.height / 100 * 2 + 0.3, 2)

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
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
        return super().expense_coat()

class Costum(Clothes):
    def __init__(self, height):
        self.height = height
    @property
    def expense_costum(self):
        return super().expense_costum()
    def expense_coat(self):
        pass

coat_1 = Coat(62)
costum_1 = Costum(175)
print(f'Расход ткани на костюм, м -\t {costum_1.expense_costum}')
print(f'Расход ткани на пальто, м -  {coat_1.expense_coat()}')
print(f'Общий расход ткани, \tм -\t {round(costum_1.expense_costum + coat_1.expense_coat(), 2)}')
