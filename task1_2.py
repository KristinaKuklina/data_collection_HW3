""" 
1. Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе.
2. Загрузите данные который вы получили на предыдущем уроке путем скрейпинга 
сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
3. Поэкспериментируйте с различными методами запросов.
"""

import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017')

# Выбор БД и коллекции
db = client['books']
collection = db['list_books']

# Чтение файла JSON
with open('books_data.json', 'r') as file:
    data = json.load(file)

# Вставка данных в коллекцию MongoDB
for item in data:
    collection.insert_one(item)

# Количество документов в коллекции
doc_count = collection.count_documents({})
print(f'Количество документов в коллекции: {doc_count}')

# Названия книг, стоимость которых >+ 40 фунтов и которых более 10 в наличии
query = {'Price, £': {"$gte": 45}, 'Count': {'$gt': 20}}
projection = {'Name': 1, '_id': 0}
names_query = collection.find(query, projection)
print(f'Количество книг по запросу 1: {collection.count_documents(query)}')
print('Названия книг стоимостью >= 40, в наличии более 10')
for doc in names_query:
    print(doc['Name'])