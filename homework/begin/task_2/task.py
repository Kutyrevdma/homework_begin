# Домашнее задание к лекции 1.2 «Условные конструкции. Операции сравнения»
# Задача №1
#
# Задачи на hackerrank:
# Решить задачу на hackerrank "Python If-Else"
# Ссылку на аккаунт приложить в личном кабинете.
# Задача №2
#
# На лекции мы рассматривали пример для военкомата. Сейчас мы знаем мы про его рост. Расширить это приложение следующим условиями:
#
#     Проверка на возраст призывника;
#     Количество детей;
#     Учится ли он сейчас.
#
height = int(input('Введите Ваш рост: '))
age = int(input('Введите Ваш возраст: '))
children = input('Есть ли у Вас дети ? ').capitalize()
if children == ('Да'):
    sum_children = int(input('Сколько у Вас детей ? '))
else:
    sum_children = 0
study = input('Вы учитесь ? ').capitalize()

if (age >= 18) and (age <= 27):
    if sum_children < 2:
        if study == ('Нет'):
            if height <= 170:
                print('Танкист')
            elif height <= 185:
                print('Флот')
            elif height <= 200:
                print('Дисант')
            else:
                print('Другие войска')
        else:
            print('Отсрочка в связи с учебой')
    else:
        print('Более 2 детей')
else:
    print('Возраст не призывной')

# Задание №3
#
################################ Поиск знака зодиака ################################

month = input('Введите месяц рождения с большой буквы: ')
day = int(input('Введите день рождение: '))

################################ Вариант № 1 ################################

# if day != 0:
#     if month != 'Январь':
#         if month != 'Февраль':
#             if month != 'Март':
#                 if month != 'Апрель':
#                     if month != 'Май':
#                         if month != 'Июнь':
#                             if month != 'Июль':
#                                 if month != 'Август':
#                                     if month != 'Сентябрь':
#                                         if month != 'Октябрь':
#                                             if month != 'Ноябрь':
#                                                 if month != 'Декабрь':
#                                                     print('Ввели неверный месяц')
#                                                 else:
#                                                     if day <= 21:
#                                                         print('Стрелец')
#                                                     elif day <= 31:
#                                                         print('Козерог')
#                                                     else:
#                                                         print('Ввели неверный день')
#                                             else:
#                                                 if day <= 22:
#                                                     print('Скорпион')
#                                                 elif day <=30:
#                                                     print('Стрелец')
#                                                 else:
#                                                     print('Ввели неверный день')
#                                         else:
#                                             if day <= 23:
#                                                 print('Весы')
#                                             elif day <= 31:
#                                                 print('Скорпион')
#                                             else:
#                                                 print('Ввели неверный день')
#                                     else:
#                                         if day <= 23:
#                                             print('Дева')
#                                         elif day <= 30:
#                                             print('Весы')
#                                         else:
#                                             print('Ввели неверный день')
#                                 else:
#                                     if day <= 23:
#                                         print('Лев')
#                                     elif day <= 31:
#                                         print('Дева')
#                                     else:
#                                         print('Ввели неверный день')
#                             else:
#                                 if day <= 22:
#                                     print('Рак')
#                                 elif day <= 31:
#                                     print('Лев')
#                                 else:
#                                     print('Ввели неверный день')
#                         else:
#                             if day <= 21:
#                                 print('Близнецы')
#                             elif day <= 30:
#                                 print('Рак')
#                             else:
#                                 print('Ввели неверный день')
#                     else:
#                         if day <= 20:
#                             print('Телец')
#                         elif day <= 31:
#                             print('Близнецы')
#                         else:
#                             print('Ввели неверный день')
#                 else:
#                     if day <= 20:
#                         print('Овен')
#                     if day <= 30:
#                         print('Телец')
#                     else:
#                         print('Ввели неверный день')
#             else:
#                 if day <= 20:
#                     print('Рыбы')
#                 elif day <= 31:
#                     print('Овен')
#                 else:
#                     print('Ввели неверный день')
#         else:
#             if day <= 18:
#                 print('Водолей')
#             elif day <= 29:
#                 print('Рыбы')
#             else:
#                 print('Ввели неверный день')
#     else:
#         if day <= 20:
#             print('Козерог')
#         elif day <= 31:
#             print('Водолей')
#         else:
#             print('Ввели неверный день')
# else:
#     print('День не может равнятся 0')

################################ Вариант № 2 ################################

# if month == 'Январь':
#     if day <= 20:
#       print('Козерог')
#     else :
#       print('Водолей')

# elif month == 'Февраль':
#     if day <= 18:
#       print('Водолей.')
#     else :
#       print('Рыбы.')

# elif month == 'Март':
#     if day <= 20:
#       print('Рыбы')
#     else :
#       print('Овен')

# elif month == 'Апрель':
#     if day <= 20:
#       print('Овен')
#     else :
#       print('Телец')

# elif month == 'Май':
#     if day <= 20:
#       print('Телец')
#     else :
#       print('Близнецы')

# elif month == 'Июнь':
#     if day <= 20:
#       print('Близнецы')
#     else :
#       print('Рак')

# elif month == 'Июль':
#     if day <= 22:
#       print('Рак')
#     else :
#       print('Лев')

# elif month == 'Август':
#     if day <= 22:
#       print('Лев')
#     else :
#       print('Дева')

# elif month == 'Сентябрь':
#     if day <= 22:
#       print('Дева')
#     else :
#       print('Весы')

# elif month == 'Октябрь':
#     if day <= 23:
#       print('Весы')
#     else:
#       print('Скорпион')

# elif month == 'Ноябрь':
#     if day <= 22:
#       print('Скорпион')
#     else :
#       print('Стрелец')

# elif month == 'Декабрь':
#     if day <= 21:
#       print('Стрелец')
#     else :
#       print('Козерог')

# else:
#     print('Ввели неверный месяц')

################################ Вариант № 3 ################################

# if False == (0 < day <= 31):
#     print('В месяце 31 день')

# elif True  == ((month == 'Январь')  and (day >= 20)) or ((month == 'Февраль') and (day <= 18)):
#     print('Водолей')

# elif True == ((month == 'Февраль') and (day >= 19)) or ((month == 'Март') and (day <= 20)):
#     print('Рыбы')

# elif True == ((month == 'Март') and (day >= 21)) or ((month == 'Апрель') and (day <= 20)):
#     print('Овен')

# elif True == ((month == 'Апрель') and (day >= 21)) or ((month == 'Май') and (day <= 20)):
#     print('Телец')

# elif True == ((month == 'Май') and (day >= 21)) or ((month == 'Июнь') and (day <= 21)):
#     print('Близнецы')

# elif True == ((month == 'Июнь') and (day >= 22)) or ((month == 'Июль') and (day <= 22)):
#     print('Рак')

# elif True == ((month == 'Июль') and (day >= 23)) or ((month == 'Август') and (day <= 23)):
#     print('Лев')

# elif True == ((month == 'Август')  and (day >= 24)) or ((month == 'Сентябрь') and (day <= 23)):
#     print('Дева')

# elif True == ((month == 'Сентябрь')and (day >= 24)) or ((month == 'Октябрь') and (day <= 23)):
#     print('Весы')

# elif True == ((month == 'Октябрь') and (day >= 24)) or ((month == 'Ноябрь') and (day <= 22)):
#     print('Скорпион')

# elif True == ((month == 'Ноябрь')  and (day >= 23)) or ((month == 'Декабрь') and (day <= 21)):
#     print('Стрелец')

# elif True == ((month == 'Декабрь') and (day >= 22)) or ((month == 'Январь') and (day <= 20)):
#     print('Козерог!')

# else:
#     print('Вы указали неверно месяц')

################################ Вариант № 3-1 (с форматированием строк) ################################

if 0 < day >= 31:
    print('В месяце 31 день')

elif ((month == 'Январь') and (day >= 20)) or \
        ((month == 'Февраль') and (day <= 18)):
    print('Водолей')

elif ((month == 'Февраль') and (day >= 19)) or \
        ((month == 'Март') and (day <= 20)):
    print('Рыбы')

elif ((month == 'Март') and (day >= 21)) or \
        ((month == 'Апрель') and (day <= 20)):
    print('Овен')

elif ((month == 'Апрель') and (day >= 21)) or \
        ((month == 'Май') and (day <= 20)):
    print('Телец')

elif ((month == 'Май') and (day >= 21)) or \
        ((month == 'Июнь') and (day <= 21)):
    print('Близнецы')

elif ((month == 'Июнь') and (day >= 22)) or \
        ((month == 'Июль') and (day <= 22)):
    print('Рак')

elif ((month == 'Июль') and (day >= 23)) or \
        ((month == 'Август') and (day <= 23)):
    print('Лев')

elif ((month == 'Август') and (day >= 24)) or \
        ((month == 'Сентябрь') and (day <= 23)):
    print('Дева')

elif ((month == 'Сентябрь') and (day >= 24)) or \
        ((month == 'Октябрь') and (day <= 23)):
    print('Весы')

elif ((month == 'Октябрь') and (day >= 24)) or \
        ((month == 'Ноябрь') and (day <= 22)):
    print('Скорпион')

elif ((month == 'Ноябрь') and (day >= 23)) or \
        ((month == 'Декабрь') and (day <= 21)):
    print('Стрелец')

elif ((month == 'Декабрь') and (day >= 22)) or \
        ((month == 'Январь') and (day <= 20)):
    print('Козерог!')

else:
    print('Вы указали неверно месяц')
# Разработать приложение для определения знака зодиака по дате рождения.
# Пример:
#
# Введите месяц: март
# Введите число: 6
#
# Вывод:
# Рыбы
#

# Задание №4
#
# К следующей лекции прочитать про циклы for и while