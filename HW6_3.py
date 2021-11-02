# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, n, s, p):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"junior":{"wage": 10000, "bonus": 1000}, "middle": {"wage": 20000, "bonus": 2000}, "senior": {"wage": 50000, "bonus": 5000}}


class Position(Worker):

    def get_full_name(self):
        print(f"Full name: {self.name + ' ' + self.surname}")

    def get_total_income(self):
        return f"Total income: {self._income.get(self.position,'Position not found')}"


w_1 = Position(input("Enter worker name: "), input("Enter surname name: "), input("Enter position (junior, middle, senior): "))
w_1.get_full_name()
w_1.get_total_income()
print(w_1.get_total_income())
