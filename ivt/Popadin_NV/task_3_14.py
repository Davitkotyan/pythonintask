# Задача 3. Вариант 14.
# Напишите программу, которая выводит имя "Вильгельм Аполлинарий Костровицкий", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.
# Попадин Никита Вадимович
# 22.03.2017

print ('Герой сегодняшней передачи - Вильгельм Аполлинарий Костровицкий. \nИтак, вопрос: каков литературный псевдоним Вильгельма Костровицкого?\nВаш ответ:')
q = input ()
e = 'Аполлинер'
if q == e:
	print ('Правильный ответ!')
else:
	print ('К сожалению, вы ошиблись! Правильный ответ: Аполлинер.')
input ('Нажмите Enter, чтобы выйти.')