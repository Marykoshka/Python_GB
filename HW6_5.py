# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery():

    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        Stationery.draw(self)
        print(f"Рисуем ручкой '{self.title}'.")


class Pencil(Stationery):

    def draw(self):
        Stationery.draw(self)
        print(f"Рисуем карандашом-шом-шом '{self.title}'!")


class Handle(Stationery):

    def draw(self):
        Stationery.draw(self)
        print(f"Рисуем маркером '{self.title}'.")

stat_1 = Pen(input("\nСоздаем ручку. Введите название: "))
stat_1.draw()

stat_2 = Pencil(input("\nСоздаем карашдаш. Введите название: "))
stat_2.draw()

stat_3 = Handle(input("\nСоздаем маркер. Введите название: "))
stat_3.draw()