# Задача 5. Вариант 12
# Напишите программу, которая бы при запуске случайным образом отображала название одного из двенадцати подвигов Геракла.

# Zemliachyov D.S.
# 15.03.2017

import random

creators = ['Немейский лев', 'Лернейская гидра', 'Керинейская лань' , 'Эриманфский вепрь', 'Стимфальские птицы', 'Авгиевы конюшни', 'Критский бык', 'Кони Диомеда', 'Пояс Ипполиты', 'Стадо Гериона', 'Яблоки Гесперид', 'Похищение Цербера']
n = random.randint(0, len(creators)-1)
print(creators[n])

input('\n\nНажмите Enter для выхода.')