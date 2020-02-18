# Домашнее задание к лекции 3.1 «Работа с разными форматами данных»
#
# Взять из папки 3.1.formats.json.xml файлы с новостями newsafr.json и newsafr.xml
#
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для
# каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(),
# sort или sorted. Задача №1
#
# Написать программу для файла в формате json.
# Задача №2.
#
# Написать программу для файла в формате xml.
# Задача №3
#
# К следующей лекции прочитать про протокол http и библиотеку requests
#
# Домашнее задание сдается ссылкой на репозиторий BitBucket или GitHub
#
# Не сможем проверить или помочь, если вы пришлете:
#
#     архивы;
#     скриншоты кода;
#     теоретический рассказ о возникших проблемах.

from pprint import pprint
import json
import xml.etree.ElementTree as ET
from collections import Counter

def xml_top10():

    tree = ET.parse('3.1.formats.json.xml/newsafr.xml')
    root = tree.getroot()
    items = root.findall(r'channel/item')
    all_list = list()

    for item in items:
        sor_spl_items = sorted(item.find('description').text.split())
        for s_s_item in sor_spl_items:
            if len(s_s_item) > 6:
                all_list.append(s_s_item)
                count = Counter(all_list)
    print('Top-10 XML')
    pprint(count.most_common(10))

def json_top10():
    with open('3.1.formats.json.xml/newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)
        all_list = list()
        for items in json_data['rss']['channel']['items']:
            item = items['description'].split()
            for i in item:
                if len(i) > 6:
                    all_list.append(i)
                    count = Counter(all_list)
        print('Top-10 JSON')
        pprint(count.most_common(10))

json_top10()
print()
xml_top10()