# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

salary = open("text_3.txt", "r", encoding="utf-8")
dict_workers = {}
for line in salary:
    line = list(line.split())
    dict_line = {line[0]: float(line[1]) for num in line}
    dict_workers.update(dict_line)
print(f"Содержимое файла о зарплатах: {dict_workers}")

print("\nЗарплаты следующих сотрудников составляют менее 20000 рублей: ")
for key, value in dict_workers.items():
    if value < 20000:
        print(key)

from functools import reduce

summ = reduce((lambda g_1, g_2: g_1 + g_2), dict_workers.values())
average_salary = summ / len(dict_workers)
print(f"\nСредняя зарплата по больнице: {average_salary} рублей.")