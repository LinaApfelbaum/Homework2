import csv
import pathlib
from json import dump, loads

books_path = str(pathlib.Path(__file__).parent.absolute()) + \
    '/../data/books.csv'
users_path = str(pathlib.Path(__file__).parent.absolute()) + \
    '/../data/users.json'
result_path = str(pathlib.Path(__file__).parent.absolute()) + \
    '/../data/result.json'

result = []
with open(books_path, newline='') as books_file:
    books_iter = csv.reader(books_file)
    next(books_iter)
    with open(users_path, 'r') as users_file:
        users_iter = iter(loads(users_file.read()))

        while True:
            try:
                user = next(users_iter)
            except StopIteration:
                break

            result_item = {
                "name": user['name'],
                "gender": user['gender'],
                "address": user['address'],
                "books": []
            }

            try:
                book = next(books_iter)
                result_item['books'].append({
                    "title": book[0],
                    "author": book[1],
                    "height": book[3]
                })
            except StopIteration:
                pass

            result.append(result_item)

with open(result_path, 'w') as result_file:
    dump(result, result_file, indent=4)
