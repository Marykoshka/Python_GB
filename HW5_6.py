# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("text_6.txt", "r", encoding="utf-8") as data:
    dataset = data.read().replace("-", "0")
    dataset = dataset.replace("(пр)", "")
    dataset = dataset.replace("(л)", "")
    dataset = dataset.replace("(лаб)", "")
    dataset = dataset.replace(":", "").split()
    new_dataset = []
    for i in dataset:
        if i.isdigit():
            new_dataset.append(int(i))
        else:
            new_dataset.append(i)

dict_set = {new_dataset[num]: [new_dataset[num + 1], new_dataset[num + 2], new_dataset[num + 3]] for num in
            range(0, len(new_dataset) - 1) if num % 4 == 0}
print(f"Исходный словарь: {dict_set}")

from functools import reduce

new_dict_set = {}
for key, value in dict_set.items():
    value = sum(value)
    new_dict_set.update({key: value})

print(f"Словарь-результат: {new_dict_set}")
