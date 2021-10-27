 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

with open("text_7.txt", "r", encoding="utf-8") as companies:
    all_comp = []
    for line in companies:
        line = line.split()
        all_comp.append(line)

all_profit = 0
loser_num = 0
final_dict = {}
for el in all_comp:
    profit = int(el[2]) - int(el[3])
    final_dict.update({el[0]: profit})
    if profit > 0:
        all_profit += profit
        print(f"Прибыль компании '{el[0]}' - {profit} руб.")
    else:
        loser_num += 1
        print(f"Убыток компании '{el[0]}' - {profit} руб.")

final_list = []
final_list.append(final_dict)

average_profit = all_profit / (len(all_comp) - loser_num)
final_list.append({"Average profit": average_profit})

print(f"Средняя прибыль компаний - {average_profit} руб.\n")
print(final_list)

import json

with open("text_7upd.json", "w", encoding="utf-8") as f:
    json.dump(final_list, f, ensure_ascii=False, indent=3)