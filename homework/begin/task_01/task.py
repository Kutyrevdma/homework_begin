"""Домашнее задание к лекции 1.1 «Python. Знакомство с консолью»"""
#
# Задача №1
#
# Зарегистрироваться на сайте hackerrank
# Решить задачу "Say "Hello, World!" With Python"
# Решить задачу "Arithmetic Operators"
# Ссылку на аккаунт приложить в личном кабинете.
#
# Задача №2
#
# Нужно разработать приложение для финансового планирования.
# Приложение учитывает сколько уходит на ипотеку, "на жизнь" и сколько нужно отложить на пенсию.
# Пользователь вводит заработанную плату в месяц.
# Сколько процентов от зп уходит на ипотеку.
# Сколько процентов от зп уходит "на жизнь".
# Сколько раз приходит премия в год.
# Остальная часть заработанной платы откладывается на пенсию.
# Также пользователю приходит премия в размере зарплаты, от которой половина уходит на отпуск, а вторая половина откладывается.
# Программа должна учитывать сколько премий было в год.
# Нужно вывести сколько денег тратит пользователь на ипотеку и сколько он накопит за год.
# Пример:
#
# Введите заработанную плату в месяц: 100000
# Введите сколько процентов уходит на ипотеку: 30
# Введите сколько процентов уходит на жизнь: 50
# Введите количество премий за год: 2
#
# Вывод:
# На ипотеку было потрачено: 360000 рублей
# Было накоплено: 340000 рублей
#
salary_month = int(input('Введите заработную плату в месяц: '))
percent_mortgage = int(input('Введите сколько процентов уходит на ипотеку: '))
percent_life = int(input('Введите сколько процентов уходит на жизнь: '))
quantity_bonus = int(input('Введите количество премий за год: '))

sum_mortagage = ((salary_month*percent_mortgage)/100)
sum_life = ((salary_month*percent_life)/100)
pension = salary_month-sum_mortagage-sum_life

bonus = salary_month
bonus_year = bonus*quantity_bonus
vacation = bonus_year/2
deferred = bonus_year/2

mortgage_year = sum_mortagage*12
accumulation = (deferred+pension*12)

print('Вывод:')
print(f'На ипотеку было потрачено: {mortgage_year} рублей')
print(f'Было накоплено: {accumulation} рублей')
# Задание №3
#
# К следующей лекции прочитать про условия
#
# Инструкция по выполнению домашнего задания:
#
#     Зарегистрируйтесь на сайте Repl.IT.
#     Перейдите в раздел my repls.
#     Нажмите кнопку Start coding now!, если приступаете впервые, или New Repl, если у вас уже есть работы.
#     В списке языков выберите Python.
#     Код пишите в левой части окна.
#     Посмотреть результат выполнения файла можно, нажав на кнопку Run. Результат появится в правой части окна.
#     После окончания работы нажмите кнопку Share и скопируйте ссылку из поля Share link.
#     В личном кабинете на сайте netology.ru в поле комментария к домашней работе вставьте скопированную ссылку и отправьте работу на проверку.
#
# Никаких файлов прикреплять не нужно.