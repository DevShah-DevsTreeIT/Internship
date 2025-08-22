# SQLite Database Setup:- Create a database with tables for a simple inventory system

import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create tables
command1 = """
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
"""
command2 = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER,
    price REAL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
"""
cursor.execute(command1)
cursor.execute(command2)

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# it show columns of products
cursor.execute("PRAGMA table_info(products);")
columns = cursor.fetchall()

print("\nProducts table columns:")
for col in columns:
    print(col)

# cursor.execute("DROP TABLE IF EXISTS  category")   #used to drop any table 

conn.commit()
conn.close()
