# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("user_file.txt", "w", encoding="utf-8") as u_f:
   while True:
      line = input("Введите строку или нажмите Enter для завершения ввода: ")
      if line == "":
         print("Ввод завершен")
         break
      else:
         print(line, file=u_f)

# ========================Задача 2=============================
# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

plush = open("text_7.txt", "r", encoding="utf-8")

sum_count = 0
for i, line in enumerate(plush, 1):
    for count, word in enumerate(line.split(), 1):
        sum_count += 1
    print("{} строка содержит {} слово/слов. Содержание строки: {}".format(i, count, line), end="")
print(f"\nОбщее количество строк - {i}. Общее количество слов - {sum_count}.")

plush.close()