class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернула на{self.direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def check_police(self):
        print(f"Полицейская: {self.is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 60 else print("Превышена допустимая скорость")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 40 else print("Превышена допустимая скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def check_police(self):
        print(f"Полицейская: {self.is_police}")


q, w, e, r, t = Car(40, "Белая", "Audi"), TownCar(40, "Черная", "BMW"), SportCar(40, "Желтая", "Lamborghini"), \
                WorkCar(40, "Вишневая", "Lada"), PoliceCar(40, "Серая", "Skoda")

q.go(), q.turn("лево"), q.stop()
q.show_speed(), q.check_police()

print(f"Марка: {q.name}, Цвет: {q.color}, Скорость: {q.speed}, Полицейская: {q.is_police}")
