# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

count_list = open("text_4.txt", "r")
data = count_list.read()
if "One" or "Two" or "Three" or "Four" in data:
    data = data.replace("One", "Один")
    data = data.replace("Two", "Два")
    data = data.replace("Three", "Три")
    data = data.replace("Four", "Четыре")
print(data)
count_list.close()

with open("txt_4_update.txt", "w", encoding="utf-8") as new_list:
        print(data, file=new_list)
