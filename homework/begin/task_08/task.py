# Домашнее задание к лекции 2.4 «Открытие и чтение файла, запись в файл»
#
# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...
#
# Пример(файл в папке 2.4.files):
#
# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт
#
# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл
#
# Запеченный картофель
# 3
# Картофель | 1 | кг
# Чеснок | 3 | зубч
# Сыр гауда | 100 | г
#
# Фахитос
# 5
# Говядина | 500 | г
# Перец сладкий | 1 | шт
# Лаваш | 2 | шт
# Винный уксус | 1 | ст.л
# Помидор | 2 | шт
#
#     В одном файле может быть произвольное количество блюд.
#     Читать список рецептов из этого файла.
#     Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
#
# Задача №1
#
# Должен получится следующий словарь
#
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
#
# Задача №2
#
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
# get_shop_list_by_dishes(dishes, person_count)
#
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
#
# Обратите внимание, что ингредиенты могут повторяться
# Задача №3
#
# Для подготовки к следующей лекции прочитайте про менеджер контекста.
#
# Домашнее задание сдается ссылкой на репозиторий BitBucket или GitHub
#
# Не сможем проверить или помочь, если вы пришлете:
#
#     архивы;
#     скриншоты кода;
#     теоретический рассказ о возникших проблемах.

from pprint import pprint

cook_book = dict()
with open('recipes.txt', encoding='UTF-8') as f:
    while True:
        name_dish = f.readline().strip()
        if not name_dish:
            break
        cook_book[name_dish] = list()
        count_ingredient = int(f.readline().strip())

        for i in range(count_ingredient):
            ingredients = f.readline().strip().split(' | ')
            cook_book[name_dish].append(
                {'ingredients_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]})

            count_ingredient -= 1
        f.readline()
pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    slovar = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_ingredient = dict(ingredient)
            new_ingredient['quantity'] *= person_count
            if new_ingredient['ingredients_name'] not in slovar:
                slovar[new_ingredient['ingredients_name']] = new_ingredient
            else:
                slovar[new_ingredient['ingredients_name']]['quantity'] += new_ingredient['quantity']

    for j1,j2 in slovar.items():
        j2.pop('ingredients_name')
    pprint(slovar)


dishes = ['Запеченный картофель', 'Утка по-пекински']
person_count = 10
get_shop_list_by_dishes(dishes, person_count)