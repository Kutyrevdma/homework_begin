# chars = [1,2,3]
# for char in chars:
#     print(char)
#
# char_list = [1,2,3]
# iter_chars = char_list.__iter__()
# print('-----')
# char = iter_chars.__next__()
# print(char)
# char = iter_chars.__next__()
# print(char)
# char = iter_chars.__next__()
# print(char)
# char = iter_chars.__next__()
# print(char)


# class MyRange:
#
#     def __init__(self, start, end):
#         self.start = start - 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start == self.end:
#             raise StopIteration
#         return self.start
#
#
# for item in MyRange(1, 5):
#     print(item)

import requests
#
#
# class CheckSite:
#
#     def __init__(self, path):
#         self.path = path
#         self.file = open(self.path, encoding='utf-8')
#         self.session = requests.Session()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         url = self.file.readline().strip()
#         if not url:
#             raise StopIteration
#         response = self.session.get(f'http://{url}')
#         status_code = response.status_code
#         return {url: status_code}
#
# if __name__ == '__main__':
#     for url_status in CheckSite('sites.list.py'):
#         print(url_status)

def check_site(path):
    session = requests.Session()
    with open(path, encoding='utf-8') as hosts_file:
        for i, url in enumerate(hosts_file):
            url = url.strip()
            status = session.get(f'http://{url}').status_code
            yield {url: status}
            print(i)

if __name__ == '__main__':
    for url_status in check_site('sites.list.py'):
        print(url_status)