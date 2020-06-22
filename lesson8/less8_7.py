class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.compl = complex(a, b)

    def __add__(self, other):
        return Complex_number(self.a + other.a, self.b +other.b)

    def __mul__(self, other):
        return Complex_number(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f"{self.compl}"


# Вводим данные
complex_1 = Complex_number(2, 5)
complex_2 = Complex_number(3, -6)
print(complex_1)
print(complex_2)

# Проверка
c = complex('2+5j')
d = complex('3-6j')

print(f'Проверка сложения - {c + d}') # Проверка
print(complex_1 + complex_2)
print(f'Проверка умножения - {c*d}')
print(complex_1 * complex_2)
