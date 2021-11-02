# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

from random import choice
class Car:
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p
    def car_go(self):
        print(f"\n{self.color} автомобиль {self.name} поехал.")

    def car_stop(self):
        print(f"{self.color} автомобиль {self.name} остановился.")

    def car_direction(self):
        print(f"Автомобиль {self.name} двигается {choice(['налево', 'направо', 'прямо', 'назад'])}.")

    def show_speed(self):
        print(f"Cкорость автомобиля (км/ч): {self.speed}")


class TownCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f"Вы городской автомобиль. Скорость превышена на {self.speed - 60} км/ч. Снизьте скорость.")

class WorkCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f"Вы рабочий автомобиль. Скорость превышена на {self.speed - 40} км/ч. Снизьте скорость.")


class SportCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        print(f"Вы гоночный автомобиль. Скорость превышена на {self.speed - 60} км/ч. Но пофиг, чувак, ты на болиде!")

class PoliceCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.is_police:
            print(f"Скорость машины {self.speed} км/ч. Но мы полиция, нам положено.")
        else:
            print(f"Оборотни в погонах, ату их, ату!")


car_1 = TownCar(65, "Белый", "Honda", False)
car_1.car_go()
car_1.car_stop()
car_1.car_direction()
car_1.show_speed()

car_2 = WorkCar(50, "Серебристый", "Kia", False)
car_2.car_go()
car_2.car_stop()
car_2.car_direction()
car_2.show_speed()

car_3 = SportCar(120, "Желтый", "Ferrari", False)
car_3.car_go()
car_3.car_stop()
car_3.car_direction()
car_3.show_speed()

car_4 = PoliceCar(90, "Белый с мигалками", "Ford Focus", True)
car_4.car_go()
car_4.car_stop()
car_4.car_direction()
car_4.show_speed()

car_4 = PoliceCar(100, "С закосом под полицию", "Ford Focus", False)
car_4.car_go()
car_4.car_stop()
car_4.car_direction()
car_4.show_speed()
