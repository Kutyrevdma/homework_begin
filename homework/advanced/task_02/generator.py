import hashlib


def md5hash(file):
    with open(file, 'rt', encoding='utf-8') as file:
        for line in file:
            result_line = hashlib.md5(line.encode())
            yield result_line.hexdigest()


if __name__ == '__main__':
    for data in md5hash('countries.json'):
        print(data)