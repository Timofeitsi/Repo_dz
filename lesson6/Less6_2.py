class Road:
    def __init__(self):
        self._length = int(input('Введите длину дороги в метрах - '))
        self._width = int(input('Введите ширину дороги в метрах - '))
        #self.massa()

    def massa(self):
        print(f"Масса асфальта - {self._length * self._width * 25 * 5/1000} тонн")

road = Road()
road.massa()