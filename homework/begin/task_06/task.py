# Домашнее задание к лекции 2.2 «Классы и их применение в Python»
#
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
#     гусей "Серый" и "Белый"
#     корову "Маньку"
#     овец "Барашек" и "Кудрявый"
#     кур "Ко-Ко" и "Кукареку"
#     коз "Рога" и "Копыта"
#     и утку "Кряква"
#
# Со всеми животными вам необходимо как-то взаимодействовать:
#
#     кормить
#     корову и коз доить
#     овец стричь
#     собирать яйца у кур, утки и гусей
#     различать по голосам(коровы мычат, утки крякают и т.д.)
#
# Задача №1
#
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
# Задача №2
#
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
# Задача №3
#
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
#     Необходимо посчитать общий вес всех животных(экземпляров класса);
#     Вывести название самого тяжелого животного.
#
# Задача №4
#
# Для подготовки к следующей лекции прочитайте про исключения.

class Animal:
    food = 'воздух'
    all_weight = 0
    list_animal = list()
    max_weight = 0

    def __init__(self,name, weight):
        self.name = name
        self.weight = weight
        Animal.all_weight += weight
        Animal.max_weight = weight
        Animal.list_animal.append(self)

    def feed(self):
        self.food = print(f'{self.name} ест {self.food}')

    def voice(self, voice='тишина'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

    def __add__(self, other):
        return self.weight + other.weight

    def __repr__(self):
        return (self.name)

    def __gt__(self, other):
        return self.weight > other.weight

class Poultry(Animal):
    list_popultry = list()
    food = 'зёрна'
    egg = 0
    all_egg = 0

    def __init__(self,name, weight):
        super().__init__(name,weight)
        Poultry.list_popultry.append(self)

    def take_egg(self, value):
        self.egg += value
        print(f'Собрано у {self.name} - {self.egg} яиц')
        Poultry.all_egg += value

class Chicken(Poultry):

    def voice(self, voice='Kukarekuuuuuuuuuuu'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

class Geese(Poultry):

    def voice(self, voice='Ga-Ga'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

class Duck(Poultry):

    def voice(self, voice='Quack Quack'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

class Cattle(Animal):
    list_cattle = list()
    food = 'сено'
    milk = 0 # l
    all_milk = 0

    def __init__(self,name, weight):
        super().__init__(name,weight)
        Cattle.list_cattle.append(self)

    def take_milk(self, value):
        self.milk += value
        print(f'Собрано у {self.name} - {self.milk} литр молока')
        Cattle.all_milk += value

class Cow(Cattle):

    def voice(self, voice='Myyyy-Myyyy'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

class Goat(Cattle):

    def voice(self, voice='Meee'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

class Sheep(Animal):
    list_sheep = list()
    food = 'солома'
    wool = 0 # кг
    all_wool = 0

    def __init__(self,name, weight):
        super().__init__(name,weight)
        Sheep.list_sheep.append(self)

    def take_wool(self, value):
        self.wool += value
        print(f'Собрано у {self.name} - {self.wool} кг шерсти')
        Sheep.all_wool += value

    def voice(self, voice='Be-Be'):
        self.voice = print(f'{self.name} гороворит: "{voice}"')

"""Создаем объекты"""

# #Гуси
goose_grey = Geese('Серый', 1)
goose_white = Geese('Белый', 5)

# Куры
chicken_ko_ko = Chicken('Ко-Ко', 1)
chicken_kykareky = Chicken('Кукареку', 3)

# Утка
duck_krakra = Duck('Кряква', 7)

# Коровы
cow_manka = Cow('Манька', 50)

# Коза
goat_roga = Goat('Рога', 2)
goat_kopeta = Goat('Копыта', 2)

# Овцы
sheep_barashek = Sheep('Барашек', 5)
sheep_kydra = Sheep('Кудрявый', 1)

"""Животный кушают"""
print('-----------------------------------')
print('---------Животные говорят----------')
print('-----------------------------------')
for i in Animal.list_animal:
    i.voice()
print('-----------------------------------')
print('----------Животный кушают----------')
print('-----------------------------------')
for i in Poultry.list_popultry:
     i.feed()
for i in Cattle.list_cattle:
     i.feed()
for i in Sheep.list_sheep:
     i.feed()

print('-----------------------------------')
print('--------Собирают у животных--------')
print('-----------------------------------')

# Гуси
goose_grey.take_egg(50)
goose_white.take_egg(1)

# Куры
chicken_ko_ko.take_egg(7)
chicken_kykareky.take_egg(10)

# Утка
duck_krakra.take_egg(1)

# Коровы
cow_manka.take_milk(3)

# Коза
goat_roga.take_milk(1)
goat_kopeta.take_milk(1)

# Овцы
sheep_barashek.take_wool(1)
sheep_kydra.take_wool(1)

print('-----------------------------------')
print('---------- Результаты: ------------')
print('-----------------------------------')
print(f'Список всех животных - {Animal.list_animal}')
print(f'Список всех домашних птиц - {Poultry.list_popultry}')
print(f'Список всех крупный рогатый скот - {Cattle.list_cattle}')
print(f'Список всех овец - {Sheep.list_sheep}')
print('-----------------------------------')
print('-------- Сборы провианта ----------')
print('-----------------------------------')
print(f'Всего яиц собранно - {Poultry.all_egg} шт')
print(f'Всего молока собранно - {Cattle.all_milk} л')
print(f'Всего шерсти собранно - {Sheep.all_wool} кг')
print('-----------------------------------')
print('------ Общий вес животных --------')
print('-----------------------------------')
print(f'Вес всех животных - {Animal.all_weight} кг')
print('-----------------------------------')
print('----- Самое тяжелое животное ------')
print('-----------------------------------')
max_weight = max(Animal.list_animal)
print(f'Самое тяжелое животное - {max_weight.name}')
print('-----------------------------------')

Бычок = Cattle('Бычок', 100)

Бычок.take_milk(10)
Бычок.feed()