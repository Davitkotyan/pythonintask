# Задача 3. Вариант 8.
# Напишите программу, которая выводит имя "Борис Николаевич Бугаев", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Ermachenkov E. M.
# 28.03.2017

q = 'Борис Николаевич Бугаев'
p = 'Андрей Белый'
print(q,'\nВведите его псевдоним')
k = input ()
if k==p:
	print('Вы ответили правильно', q, '-',p)
else:
	print('Вы ответили неверно')
input('Нажмите Enter для выхода')
