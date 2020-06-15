class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationery):
     def draw(self):
        print(f"Ручкой только пишем")

class Pencil(Stationery):
    def draw(self):
        print(f"Карандашом чертим и рисуем")

class Handle(Stationery):
    def draw(self):
        print(f"Маркером выделяем")

pen = Stationery('Чтобы рисовать')
pen.draw()
pen2 = Pen('Чтобы писать')
pen2.draw()
pencil = Pencil('Чтобы чертить и рисовать')
pencil.draw()
handle = Handle('Чтобы выделять')
handle.draw()
print(handle.title)