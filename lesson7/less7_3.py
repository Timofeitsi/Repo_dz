class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if (self.num - other.num) < 0:
            return 'Вычитание невозможно'
        else:
            return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def __str__(self):
        return f"{self.num}"

    def make_order(self, el_to_row):
        row = [('*' * 5) for x in range(self.num // el_to_row)]
        row.append('*' * (self.num % el_to_row))
        print('\n'.join(row))

cell_1 = Cell(43)
cell_2 = Cell(12)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_1.make_order(8)
