class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._finance = dict.fromkeys(['wage', 'bonus'])
        self._finance['wage'] = int(wage)
        self._finance['bonus'] = int(bonus)

class Position(Worker):
    def get_full_name(self):
        print(f"Сотрудник - {self.name} {self.surname}")
    def get_total_income(self):
        print(f"Доход - {self._finance['wage'] + self._finance['bonus']} тугриков")


Worker1 = Position('Иван', 'Петров', 'Слесарь', 1000, 2000)
Worker1.get_full_name()
Worker1.get_total_income()
print(Worker1._finance)
print(Worker1.position)
