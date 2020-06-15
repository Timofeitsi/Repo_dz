import random
class Car:
    def __init__(self, auto_name, auto_color, speed, is_police=None):
        self.auto_speed = speed
        self.auto_color = auto_color
        self.auto_name = auto_name
        self.is_police = bool(is_police)

    def go(self, acceleration):
        self.current_speed += acceleration
        print(f"{self.auto_name} ускорилась на {acceleration} км.ч.")
        if self.current_speed > self.auto_speed:
            self.current_speed = self.auto_speed
            print(f"{self.auto_name}, вы технически не можете двигаться быстрее {self.auto_speed} км.ч.")
        self.show_speed()

    def stop(self):
        print(f"{self.auto_name} остановилась")
        self.current_speed = 0

    def turn(self):
        print(f"{self.auto_name} двигается {random.choice(['forward', 'left', 'right', 'back'])}")

    def show_speed(self):
        print(f"Текущая скорость {self.auto_name} - {self.current_speed} км.ч.")

class TownCar(Car):
    def __init__(self, auto_name, auto_color, speed, is_police=None):
        super().__init__(auto_name, auto_color, speed, is_police)
        self.speed_limit = 60
        self.current_speed = 0
    def show_speed(self):
        print(f"Текущая скорость {self.auto_name} - {self.current_speed} км.ч.")
        if self.current_speed > self.speed_limit:
            print(f"\033[31m{self.auto_color} {self.auto_name} Вы превысили скорость на {self.current_speed - self.speed_limit} км.ч.")
            print(f"Снизьте скорость до {self.speed_limit} км.ч.\033[0m")

class SportCar(Car):
    def __init__(self, auto_name, auto_color, speed, is_police=None):
        super().__init__(auto_name, auto_color, speed, is_police)
        self.speed_limit = 60
        self.current_speed = 0

class WorkCar(Car):
    def __init__(self, auto_name, auto_color, speed):
        super().__init__(auto_name, auto_color, speed)
        self.speed_limit = 40
        self.current_speed = 0

    def show_speed(self):
        print(f"Текущая скорость {self.auto_name} - {self.current_speed} км.ч.")
        if self.current_speed > self.speed_limit:
            print(f"\033[31m{self.auto_color} {self.auto_name} Вы превысили скорость на {self.current_speed - self.speed_limit} км.ч.")
            print(f"Снизьте скорость до {self.speed_limit} км.ч.\033[0m")

class PoliceCar(Car):
    def __init__(self, auto_name, auto_color, speed, is_police):
        super().__init__(auto_name, auto_color, speed, is_police)
        self.speed_limit = 150
        self.current_speed = 0

car1 = TownCar('Niva', 'red', 80)
car1.go(56)
car1.turn()
car1.go(20)
car1.stop()

car2 = SportCar('Porsche', 'red', 160)
car2.go(56)
car2.go(20)
car2.go(20)
car2.go(20)
car2.turn()
car2.go(20)
car2.stop()

car3 = WorkCar('Трактор', 'синий', 50)
car3.go(20)
car3.go(20)
car3.go(20)
car3.turn()
car3.stop()
print(car1.is_police)
print(car3.is_police)

car4 = PoliceCar('Porsche', 'red', 160, 1)
print(car4.is_police)
print(type(car4.is_police))