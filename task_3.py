from pymongo import MongoClient
import json

# создание экземпляра клиента
client = MongoClient()

# подключение к базе данных и коллекции
db = client['books']
collection = db['list_books']

# Названия книг, стоимость которых >= 45 фунтов и которых более 15 в наличии
query = {'Price, £': {"$gte": 45}, 'Count': {'$gt': 15}}
projection = {'Name': 1, '_id': 0}
names_query = collection.find(query, projection)
print(f'Количество книг по запросу 1: {collection.count_documents(query)}')
print('Названия книг стоимостью >= 40, в наличии более 10')
for doc in names_query:
    print(doc['Name'])

# Количество книг, которых нет в наличии
query = {'Count': {'$eq': 0}}
print(f'Количество книг, которых нет в наличии: {collection.count_documents(query)}')

# Количество книг в единственном экземпляре
query = {'Count': {'$eq': 1}}
print(f'Количество книг в единственном экземпляре: {collection.count_documents(query)}')

# Использование оператора $regex
query = {"Name": {"$regex": "[Ll]ove"}}
print(f"Количество книг, содержащих 'love' или 'Love': {collection.count_documents(query)}")