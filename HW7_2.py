# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Dress:
    def __init__(self, v, h):
        self.vol = v
        self.height = h

    def sing_song(self):
        print("И такая дребедень целый день\n")


class Coat(Dress):
    def __init__(self, v, h):
        super().__init__(v, h)

    def coat_amount(self):
        self.c_amount = self.vol / 6.5 + 0.5
        # Dress.gen_amount.append(self.c_amount)
        print(f"Количество ткани на пальто: {self.c_amount:.2f} м.")

    def sing_song(self):
        print("Через день\n")

class Suit(Dress):
    def __init__(self, v, h):
        super().__init__(v, h)

    @property
    def suit_amount(self):
        self.s_amount = 2 * self.height + 0.3
        # Dress.gen_amount.append(self.s_amount)
        return f"Количество ткани на костюм: {round(self.s_amount, 2)} м."

    def sing_song(self):
        print("Каждый день\n")

    @property
    def general_amount(self):
        return f"Общее количество ткани: {round((self.vol / 6.5 + 0.5 + 2 * self.height + 0.3), 1)} м."


person_1 = Dress(44, 1.62)
person_1.sing_song()
person_1 = Coat(44, 1.62)
person_1.coat_amount()
person_1.sing_song()
person_1 = Suit(44, 1.62)
print(person_1.suit_amount)
print(person_1.general_amount)
person_1.sing_song()


