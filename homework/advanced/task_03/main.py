# Создать приложение "Телефонная книга". класс Contact.
class Contact:

    def __init__(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):

        # Имя, фамилия, телефонный номер - обязательные поля
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        # Избранный контакт - необязательное поле. По умолчанию False;
        self.favorite_contact = favorite_contact

        # Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо
        # использовать *args, **kwargs.
        self.args_list = []
        for arg in args:
            self.args_list.append(arg)

        self.kwargs_dict = {}
        for item_name, item_value in kwargs.items():
            self.kwargs_dict[item_name] = item_value

    # Переопределить "магический" метод str для красивого вывода контакта.
    def __str__(self):
        if self.favorite_contact:
            favorite_contact_ru = 'Да'
        else:
            favorite_contact_ru = 'Нет'

        return str(
            "Имя: " + self.first_name + "\n" +
            "Фамилия: " + self.last_name + "\n" +
            "Телефон: " + self.phone_number + "\n" +
            "В избранных: " + favorite_contact_ru + "\n" +
            "Дополнительная информация: " + "\n" +
            "\t" + '\n\t'.join(self.args_list) + "\n" +
            "\t" + "\n\t".join('{}: {}'.format(item_name, item_value) for item_name, item_value
                               in sorted(self.kwargs_dict.items()))
        )


# класс PhoneBook.
class PhoneBook:

    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name
        self.work_phonebook = []

    @staticmethod
    def help():
        print('\ndef get_contacts(phonebook) - Вывод контактов из телефонной книги\n'
              'def create_contact(contact, phonebook) - Добавление нового контакта\n'
              'def delete_contact_by_number(phone_number, phonebook) - Удаление контакта по номеру телефона\n'
              'def get_favorite_contacts(phonebook) - Поиск всех избранных номеров\n'
              'def get_contact_by_name(phonebook, first_name, last_name) - Поиск контакта по имени и фамилии\n')

    # Вывод контактов из телефонной книги
    def get_contacts(self):
        contacts = []
        for contact in self.work_phonebook:
            contacts.append(contact)
        return contacts

    # Добавление нового контакта
    def create_contact(self, contact):
        self.work_phonebook.append(contact)

    # Удаление контакта по номеру телефона
    def delete_contact_by_number(self, phone_number):
        if contact.__dict__['phone_number'] == phone_number:
            self.work_phonebook.remove(contact)
        return self.work_phonebook

    # Поиск всех избранных номеров
    def get_favorite_contacts(self):
        favorite_contacts = []
        for contact in self.work_phonebook:
            if contact.__dict__['favorite_contact']:
                favorite_contacts.append(contact)
        return favorite_contacts

    # Поиск контакта по имени и фамилии
    def get_contact_by_name(self, first_name, last_name):
        found_contacts = []
        for contact in self.work_phonebook:
            if contact.__dict__['first_name'] == first_name and (contact.__dict__)['last_name'] == last_name:
                found_contacts.append(contact)
        return found_contacts


# Создание контакта

contact_1 = Contact('Уолтер', 'Уайт', '+00000000001', True, 'Альбукерке, Orlando PI NE', '+00000000011',
                    'Учитель', telegram='@Уолтер', email='Уолтер@albuquerque.com')

contact_2 = Contact('Скайлер', 'Уайт', '+00000000002', False, 'Альбукерке, Orlando PI NE', '+00000000012',
                    'Бухгалтер', telegram='@Скайлер', email='Скайлер@albuquerque.com')

contact_3 = Contact('Джесси', 'Пинкман', '+00000000003', False, 'Альбукерке, Orlando PI NE', '+00000000013',
                    'Дилер', telegram='@Джесси', email='Джесси@albuquerque.com')

contact_4 = Contact('Хэнк', 'Шрейдер', '+00000000004', True, 'Альбукерке, Orlando PI NE', '+00000000014',
                    'Полицейский', telegram='@Хэнк', email='Хэнк@albuquerque.com')

# Создание телефонной книги

book = PhoneBook('book')

book.create_contact(contact_1)
book.create_contact(contact_2)
book.create_contact(contact_3)
book.create_contact(contact_4)

print('\nВывод контактов из телефонной книги:\n')
contacts = book.get_contacts()
for contact in contacts:
    print(contact)

print('\nУдаление контакта по номеру телефона:\n')
for contact in contacts:
    book.delete_contact_by_number('+00000000001', )

print('\nДобавление нового контакта:\n')
contacts = book.get_contacts()
for contact in contacts:
    print(contact)

print('\nПоиск всех избранных номеров:\n')
favorite_contacts = book.get_favorite_contacts()
for contact in favorite_contacts:
    print(contact)

print('Поиск контакта по имени и фамилии:')
found_contacts = book.get_contact_by_name('Джесси', 'Пинкман')
for contact in found_contacts:
    print(contact)

print('\nВывод помощи по методам класса PhoneBook')
book.help()