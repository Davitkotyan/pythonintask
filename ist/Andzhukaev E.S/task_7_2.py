# Задача 7. Вариант 2.
#1-50. Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Andzhukaev E.S.
#13.03.2017

import random,string
stars =  ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

rightAnswer = random.choice(stars)
scores = 10000
answer = ""
print("Создайте игру, в которой компьютер загадывает название"
      "одного из двенадцати созвездий, входящих в зодиакальный круг \n"\
      "а игрок должен его угадать ")
print("Чем меньше попыток вы используете, тем больше баллов заработаете.")

while answer != rightAnswer:
	answer = input("Попробуй отгадать созвездие: ")
	if answer == rightAnswer:
		print("\nВсе верно!")
		print("Вам начислено", scores,"баллов.")

	else:
		scores-=1000
		print("\nВы не угадали!!!\nПопробуйте еще раз\n\n")
input("\n\nНажмите Enter для выхода")