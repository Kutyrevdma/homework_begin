# Домашнее задание к лекции 2.1 «Функции — использование встроенных и создание собственных»
#
# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять
# ни один документ. Каталог документов хранится в следующем виде:
#
#       documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]
#
# Перечень полок, на которых находятся документы хранится в следующем виде:
#
#       directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006', '5400 028765', '5455 002299'],
#         '3': []
#       }
#
# Задача №1
#
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит; l– list –
# команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"; s – shelf –
# команда, которая спросит номер документа и выведет номер полки, на которой он находится; a – add – команда,
# которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
# на котором он будет храниться. Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции
# должны иметь выразительное название, передающие её действие.
#
# Задача №2. Дополнительная (не обязательная)
#
#     d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
#     m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
#     as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
#
# Задача №3
#
# Почитать про lambda-функции. И что такое *args и **kwargs.
# Задача №4
#
# Для подготовки к следующей лекции прочитайте про классы.

# |---------------------------------------------------------------------------------------------------------------|
# |                                                  База данных                                                  |
# |---------------------------------------------------------------------------------------------------------------|
# |---------------------------------------------------------------------------------------------------------------|
# |                                               Каталог документов                                              |
# |---------------------------------------------------------------------------------------------------------------|

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "1", "number": "1", "name": "1"}
]
# |---------------------------------------------------------------------------------------------------------------|
#                                                  Рабочие полки                                                  |
# |---------------------------------------------------------------------------------------------------------------|

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': ['1']
}


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: search_people.                                                                                        |
# |Вызвать: p                                                                                                     |
# |Назначение: команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.          |
# |---------------------------------------------------------------------------------------------------------------|

def search_people():
    # Вводим данные с клавиатуры.
    document_number_input = input('Введите номер документа: ')
    # Итерация библиотеки - documents.
    for documents_itartion in documents:
        # Проверка наличия документа в библиотеке.
        if documents_itartion['number'] == document_number_input:
            name = documents_itartion['name']
            print(f'\n{name} - Владелец документа.', end='\n\n')
            return
    print(f'\n{document_number_input} документа нет.', end='\n\n')


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: documents_list.                                                                                       |
# |Вызвать: l                                                                                                     |
# |Назначение: команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин". |
# |---------------------------------------------------------------------------------------------------------------|

def documents_list():
    # Итерация библиотеки - documents.
    for documents_itartion in documents:
        print(*documents_itartion.values(), end='\n\n')


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: documents_list.                                                                                       |
# |Вызвать: s                                                                                                     |
# |Назначение: команда, которая спросит номер документа и выведет номер полки, на которой он находится.           |
# |---------------------------------------------------------------------------------------------------------------|

def search_document():
    # Вводим данные с клавиатуры.
    document_input = input('Введите номер документа: ')
    # Итерация библиотеки - directories.
    for number_shelf_itartion, shelf_iteration in directories.items():
        # Ищем по значению документ в библиотеке.
        if document_input in shelf_iteration:
            print(f'\nВаш документ находится на полке - {number_shelf_itartion}', end='\n\n')
            return
    print(f'\nДокумента {document_input} нету на полках', end='\n\n')


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: add_documents.                                                                                        |
# |Вызвать: add                                                                                                   |
# |Назначение: команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,      |
# |            имя владельца и номер полки, на котором он будет храниться.                                        |
# |---------------------------------------------------------------------------------------------------------------|

def add_documents():
    new_type_input = input('\nВведите тип документа: ').lower()
    new_number_input = input('Введите номер документа: ')
    new_name_input = input('Введите имя и фамилию владельца документа: ').title()
    number_shelf_input = input(f'Введите полку : ')
    print()

    # Услови по достутпным полкам
    if number_shelf_input in directories:

        # Поиск по номеру документа
        for documents_itaration in documents:
            if documents_itaration['type'] == new_type_input and \
                    documents_itaration['number'] == new_number_input and \
                    documents_itaration['name'] == new_name_input:
                print('Данный документ уже имеется!', end='\n\n')
            else:
                new_document = ({'type': new_type_input, 'number': new_number_input, 'name': new_name_input})
        if new_document not in documents:
            documents.append(new_document)
            directories[number_shelf_input].append(new_number_input)

        # Вывод полки и всех документов
        for documents_itaration in documents:
            print(
                f"Тип - {documents_itaration['type']} | Номер - {documents_itaration['number']} | Владелец - {documents_itaration['name']}")
        print()
        for directories_itaration in directories:
            print(f'Полка - {directories_itaration} на полке {directories[directories_itaration]}')
    else:
        print('Такой полки нету. Но вы можете её создать с помощью команды - as.', end='\n\n')


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: delete_document.                                                                                      |
# |Вызвать: d                                                                                                     |
# |Назначение: команда, которая спросит номер документа и удалит его из каталога и из перечня полок.              |
# |---------------------------------------------------------------------------------------------------------------|

def delete_document():
    document_delete_input = input('Введите номер документа для удаления: ')
    for document_iteration in documents:
        # Поиск документа в каталоге.
        if document_iteration['number'] == document_delete_input:
            documents.remove(document_iteration)
            # Поиск документа на полке.
            for number_shelf_itartion, shelf_iteration in directories.items():
                if document_delete_input in shelf_iteration:
                    directories[number_shelf_itartion].remove(document_delete_input)
                    print(f'\nДокумент {document_delete_input} удален', end='\n\n')
                    return
    print(f'\nДокумента {document_delete_input} нету', end='\n\n')


# |-----------------------------------------------------------------------------------------------------------------|
# |Функция: move_document.                                                                                          |
# |Вызвать: m                                                                                                       |
# |Назначение: команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.|
# |-----------------------------------------------------------------------------------------------------------------|

def move_document():
    print(f'\nПолка до - {directories}\n')
    document_number_input = input('Введите номер дкоумента: ')
    shelf_number_input = input('Введите номер полки: ')
    print()
    for number_iteration, shelf_iteration in directories.items():
        if document_number_input in shelf_iteration:
            if shelf_number_input in directories.keys():
                directories[shelf_number_input].append(document_number_input)
                directories[number_iteration].remove(document_number_input)
                directories_list()
                return
            else:
                directories[number_iteration].remove(document_number_input)
                directories[shelf_number_input] = list()
                directories[shelf_number_input].append(document_number_input)
                directories_list()
                return


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: add_shelf.                                                                                      |
# |Вызвать: as                                                                                                    |
# |Назначение: команда, которая спросит номер новой полки и добавит ее в перечень.                                |
# |---------------------------------------------------------------------------------------------------------------|

def add_shelf():
    shuelf_number_input = input('Введите номер полки: ')
    if shuelf_number_input in directories.keys():
        print(f'\nПолка {shuelf_number_input} есть', end='\n\n')
    else:
        directories[shuelf_number_input] = []
        print(f'Полка - {shuelf_number_input} создана', end='\n\n')
    directories_list()


# |---------------------------------------------------------------------------------------------------------------|
# |Функция: main.                                                                                                 |
# |Вызвать: as                                                                                                    |
# |Назначение: Вызывает интерактивное меню                                       .                                |
# |---------------------------------------------------------------------------------------------------------------|

def directories_list():
    for directories_itaration in directories:
        print(f'Полка - {directories_itaration} на полке {directories[directories_itaration]}')


def main():
    while True:
        print('----------------------------------------------------------------------------------')
        print('Доступные команды:\n\
        p – команда, которая спрашивает номер документа и выводит имя человека, которому он принадлежит.\n\
        l – команда, которая выведет список всех документов.\n\
        s – команда, которая спрашивает номер документа и выводит номер полки, на которой он находится.\n\
        a – команда, которая добавит новый документ в каталог и в перечень полок.\n\
        d - команда, которая спросит номер документа и удалит его из каталога и из перечня полок.\n\
        m – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.\n\
        as - команда, которая спросит номер новой полки и добавит ее в перечень.\n\
        q - команда для выхода.\n\
        ')

        user_input = input('\nВведите команду: ').lower()
        print('----------------------------------------------------------------------------------')
        if user_input == 'p':
            search_people()
        elif user_input == 'l':
            documents_list()
        elif user_input == 's':
            search_document()
        elif user_input == 'a':
            add_documents()
        elif user_input == 'd':
            delete_document()
        elif user_input == 'as':
            add_shelf()
        elif user_input == 'm':
            move_document()
        elif user_input == 'q':
            break
        else:
            print('Вы ввели неверную команды. Попробуте снова.\n')


main()

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10006", },
    {"type": "1", "number": "1", "name": " "}
]