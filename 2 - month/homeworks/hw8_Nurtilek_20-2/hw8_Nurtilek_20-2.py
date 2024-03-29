import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price , quantity)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products  WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)

def select_all_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)

def select_product(conn):
    try:
        sql = '''SELECT * FROM products WHERE price <= 100 and quantity >= 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)

connection = create_connection('''products.db''')
create_product_table = '''
CREATE table products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print("Connected successfully!")

create_table(connection, create_product_table)

# create_product(connection, ("bread", 20.00, 5))
# create_product(connection, ("milk", 60.00, 15))
# create_product(connection, ("lays", 120.00, 7))
# create_product(connection, ("tomato", 50.00, 23))
# create_product(connection, ("coca-cola", 85.00, 67))
# create_product(connection, ("pivo", 100.00, 100))
# create_product(connection, ("kurut", 10.00, 90))
# create_product(connection, ("baclajan", 65.00, 6))
# create_product(connection, ("juce", 120.00, 5))
# create_product(connection, ("smetana", 65.00, 4))
# create_product(connection, ("ketchup", 65.00, 3))
# create_product(connection, ("bablajan", 55.55, 8))
# create_product(connection, ("sigaretes", 200.00, 50))
# create_product(connection, ("redbull", 500.00, 10))
# create_product(connection, ("meat", 400.00, 8))
# create_product(connection, ("toilet paper", 20.00, 100))

#
# select_product(connection)
# update_price(connection, (100.15, 1))
# delete_product(connection, 16)
# select_all_product(connection)