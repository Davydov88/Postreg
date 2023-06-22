import psycopg2
import csv

# Параметры подключения к базе данных
db_host = 'localhost'
db_port = '5432'
db_name = 'north_1'
db_user = 'postgres'
db_password = 'Aleksandr110460+'  # Замените на ваш пароль

# Функция для выполнения SQL-запроса
def execute_query(query):
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

# Функция для заполнения таблицы данными из CSV-файла
def insert_data_from_csv(table_name, csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            values = "', '".join(row)
            query = f"INSERT INTO {table_name} VALUES ('{values}');"
            execute_query(query)

# Заполнение таблицы employees данными
employees_csv = 'north_data/employees_data.csv'
insert_data_from_csv('employees', employees_csv)

# Заполнение таблицы customers данными
customers_csv = 'north_data/customers_data.csv'
insert_data_from_csv('customers', customers_csv)

# Заполнение таблицы orders данными
orders_csv = 'north_data/orders_data.csv'
insert_data_from_csv('orders', orders_csv)
