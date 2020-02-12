# Домашнее задание к лекции 2.5 «Менеджер контекста»
# Задача №1
#
# Необходимо реализовать менеджер контекста, печатающий на экран:
#
#     Время запуска кода в менеджере контекста;
#     Время окончания работы кода;
#     Сколько было потрачено времени на выполнение кода.
#
# Задача №2
#
# Придумать и написать программу, использующая менеджер контекста из задания 1. Если придумать не получиться,
# использовать программу из предыдущих домашних работ. Задача №3
#
# Для подготовки к следующей лекции прочитайте про форматы данных json, xml, csv.


from datetime import datetime
# """ Наивный метод """
#
# try:
#     file = open('recipes.txt', encoding='UTF-8')
#     data = file.read()
# finally:
#     # print('Конец!')
#     file.close()
#
# """ Изящный метод """
#
# with open('recipes.txt', encoding='UTF-8') as file:
#     data = file.read()
#     # print(data)

""" Мой класс """

# class MyMC:
#     def __init__(self, file_path, encoding):
#         self.file_path = file_path
#         self.encoding = encoding
#
#     def __enter__(self):
#         self.file = open(self.file_path, encoding='UTF-8')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# if __name__ == '__main__':
#     with MyMC('recipes.txt', encoding='UTF-8') as file:
#         data = file.read()
#         # print(data)

"""Это запись"""


class LogOpen:
    def __init__(self, path, encoding):
        self.path = path
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.path, 'a', encoding='UTF-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Конец!')
        if exc_type:
            self.write_log(str(exc_type))
            self.write_log(str(exc_val))
        self.file.close()

    def write_log_start(self, message):
        self.file.write(f'{datetime.now().strftime("%H.%M.%S")}'
                        f' Время начала. Ваш текст ---> {message}\n')

    def write_log_flag(self,message):
        self.file.write(f'{datetime.now().strftime("%H.%M.%S")}'
                        f' Время флага. Ваш текст ---> {message}\n')

    def write_log_finish(self, message):
        self.file.write(f'{datetime.now().strftime("%H.%M.%S")}'
                        f' Время окончания. Ваш текст ---> {message}\n')


if __name__ == '__main__':
    with LogOpen('testfile.txt', encoding='UTF-8') as log:
        a = datetime.now()
        log.write_log_start('Старт')
        for i in range(2000000):
            print(i)
            if i == 500000:
                log.write_log_flag(f'Контрольная точка в 500000 x__ > {i}')
            elif i == 1000000:
                log.write_log_flag(f'Контрольная точка в 1000000 xx_ > {i}')
            elif i == 1500000:
                log.write_log_flag(f'Контрольная точка в 1500000 xxx > {i}')
        b = datetime.now()
        c = b - a
        print(f'Потрачено времени на выполнение кода {c}')
        log.write_log_finish(f'Финиш. Потрачено времения ----> {c}')