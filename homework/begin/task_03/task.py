# Домашнее задание к лекции 1.3 «Введение в типы данных и циклы»
# Задача №1
#
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с
# одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект
# и выведем информацию в виде:
#
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
#
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будет и выведем
# пользователю предупреждение, что кто-то может остаться без пары!

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys)!= len(girls):
    print('Внимание! Кто-то остался без пары!')
else:
    boys.sort()
    girls.sort()

    print('Идеальные пары:\n')
    for pair_boy_and_girls in zip(boys, girls):
        print(f'{pair_boy_and_girls[0]} и {pair_boy_and_girls[1]}')
# Задача №2
#
# Имеется структура данных cook_book, в которой хранится информация об ингредиентах блюд и их количестве в расчете на
# одну порцию:
#
# cook_book = [
#   ['салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['майонез', 70, 'мл.'],
#       ]
#   ],
#   ['пицца',
#       [
#         ['сыр', 50, 'гр.'],
#         ['томаты', 50, 'гр.'],
#         ['тесто', 100, 'гр.'],
#         ['бекон', 30, 'гр.'],
#         ['колбаса', 30, 'гр.'],
#         ['грибы', 20, 'гр.'],
#       ],
#   ],
#   ['фруктовый десерт',
#       [
#         ['хурма', 60, 'гр.'],
#         ['киви', 60, 'гр.'],
#         ['творог', 60, 'гр.'],
#         ['сахар', 10, 'гр.'],
#         ['мед', 50, 'мл.'],
#       ]
#   ]
# ]
#
# и переменная, в которой хранится количество людей, на которых необходимо приготовить данные блюда:
#
# person = 5
#
# Необходимо вывести пользователю список покупок необходимого количества ингредиентов для приготовления блюд на
# определенное число персон в следующем виде:
#
# Салат:
# картофель, 500гр.
# морковь, 250гр.
# огурцы, 250гр.
# горошек, 150гр.
# майонез, 350мл.
#
# Пицца:
# сыр, 250гр.
# томаты, 250гр.
# тесто, 500гр.
# бекон, 150гр.
# колбаса, 150гр.
# грибы, 100гр.
#
# Фруктовый десерт:
# хурма, 300гр.
# киви, 300гр.
# творог, 300гр.
# сахар, 50гр.
# мед, 250мл.
#
# Внимание! Реализация не должна зависеть от количества блюд, их названий и количества ингредиентов в них!
person = 5
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ],
]

for name_cook in cook_book:
    print(f' {name_cook[0].capitalize()} :')
    for name_ingred in name_cook[1]:
        print(f' {name_ingred[0]}, {name_ingred[1] * person} {name_ingred[2]}')
    print('\n')
# Задание №3
#
# К следующей лекции прочитать про типы данных