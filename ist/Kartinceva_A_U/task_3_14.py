#Задача 3. Вариант 14
#Напишите программу, которая выводит имя "Вильгельм Аполлинарий Костровицкий", и запрашивает его псевдоним.
#Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Kartinceva A.U.
#12.04.17


print ("Привет! Сегодня на повестке дня Вильгельм Аполлинарий Костровицкий!")
Answer = input("\nПод каким псевдоннимом известен этот человек? Твой ответ, друг мой: ")
if Answer == "Гийом Апполинер":
	print ("Правильно! Вильгельм Аполлинарий Костровицкий " + "-" + " это Гийом Апполинер!")
else:
	print ("Ой! Попробуй снова!")

input ("\nPress Enter to exit")