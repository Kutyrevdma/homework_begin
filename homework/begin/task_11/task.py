# Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы»
#
# Исходный код для выполнения домашней работы вы найдете в папке 3.2.http.requests.
# Задача №1
#
# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
#
#     Путь к файлу с текстом;
#     Путь к файлу с результатом;
#     Язык с которого перевести;
#     Язык на который перевести (по-умолчанию русский).
#
# У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком. Функция
# должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
#
# Для переводов можно пользоваться API Yandex.Переводчик.
# *Задача №2
#
# Научиться работать с api Яндекс.Диска Написать программу, которая загружает переведенные файлы на Яндекс.Диск.
# Документация по загрузке файлов Токен можно получить на Полигоне кликнув по кнопке "Получить OAuth-токен"
#
# Домашнее задание сдается ссылкой на репозиторий BitBucket или GitHub
#
# Не сможем проверить или помочь, если вы пришлете:
#
#     архивы;
#     скриншоты кода;
#     теоретический рассказ о возникших проблемах.

import os
import requests

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20200221T210149Z.b8373ccfdc2521ac.a23aca59ad3973bd18041971f50ce7620f9babef'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

#     Путь к файлу с текстом;
#     Путь к файлу с результатом;
#     Язык с которого перевести;
#     Язык на который перевести (по-умолчанию русский).

def translate_it(file_in, file_out, lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    path_in = os.path.abspath(file_in)
    with open(path_in, 'r') as f:
        text = f.read()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang, to_lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    # print(json_)
    translate = ''.join(json_['text'])
    # print(translate)
    with open(file_out, 'w', encoding='utf-8') as f:
        f.write(translate)


if __name__ == '__main__':
    # У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком. Функция
    # должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.

    print(translate_it('DE.txt', 'RU-DE.txt', 'de'))
    print(translate_it('ES.txt', 'RU-ES.txt', 'es'))
    print(translate_it('FR.txt', 'RU-FR.txt', 'fr'))
