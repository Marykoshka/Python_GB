# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("text_for_5.5.txt", "w") as text_5:
    num_set = str([randint(1, 500) for _ in range(1, randint(5, 10))])
    text_5.write(num_set)

numbers = open("text_for_5.5.txt")

numbers_cont = numbers.read()
numbers_cont = numbers_cont[1:-1].split(", ")
numbers_cont = list(map(int, numbers_cont))
num_sum = sum(numbers_cont)
print(f"Сумма значений списка {numbers_cont} равна {num_sum}.")

numbers.close()