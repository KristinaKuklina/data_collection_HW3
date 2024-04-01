""" Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения."""
from clickhouse_driver import Client
import json

# Подключение к ClickHouse
client = Client(host='localhost',  # Use 'localhost' or '127.0.0.1' for a local server
                user='default',    # Default user, adjust if you've changed the user
                password='',       # Default installation has no password for 'default' user
                port=9000)         # Default TCP port for ClickHouse

query = f'DROP TABLE IF EXISTS books'
client.execute(query)

# Чтение файла JSON
with open('books_data.json', 'r') as file:
    data = json.load(file)

client.execute (
'''
CREATE TABLE books
(
    `Name` String,
    `Price, £` Float64,
    `Count` Int8
)
ENGINE = MergeTree
ORDER BY Name;
'''
)

client.execute('SHOW TABLES')

# Загрузка данных в таблицу 
for item in data:
    query = f"INSERT INTO books FORMAT JSONEachRow {json.dumps(item)}"
    client.execute(query)

print(client.execute('SELECT count() FROM books')[0])