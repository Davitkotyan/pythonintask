# Задача 6. Вариант 14.
# Создайте игру, в которой компьютер загадывает имя одного из трех официальных талисманов зимних Олимпийских игр 2014 года в Сочи, а игрок должен его угадать.

# Rozum R.S.
# 16.04.2017

import random

print("Программа случайным образом загадывает имя одного из трех официальных талисманов зимних Олимпийских игр, а игрок должен угадать его.")

number = random.randint(1,3)

if number == 1:
    mascot = "Леопард"
elif number == 2:
    mascot = "Белый Мишка"
elif number == 3:
    mascot = "Зайка"

answer = input("Назовите имя одного из талисманов: ")

if answer == mascot:
    print("Вы угадали!")
else:
    print("Вы не угадали!")
    print("Правильный ответ: ", mascot)

input("\nНажмите Enter для выхода.")