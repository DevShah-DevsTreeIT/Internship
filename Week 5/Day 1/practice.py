# import sqlite3

# # Connect to the database (creates it if it doesn't exist)
# conn = sqlite3.connect('inventory.db')

# # Create a cursor to interact with the DB
# cursor = conn.cursor()

# # Create the Products table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Products (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         quantity INTEGER NOT NULL,
#         price REAL NOT NULL
#     )
# ''')

# data = input("Enter your  data")


# # Insert some products
# cursor.execute('''
#     INSERT INTO Products (name, quantity, price)
#     VALUES (?, ?, ?)
# ''', ("Pen", 50, 1.20))

# cursor.execute('''
#     INSERT INTO Products (name, quantity, price)
#     VALUES (?, ?, ?)
# ''', ("Notebook", 30, 2.75))

# # Query and print all products
# cursor.execute('SELECT * FROM Products')
# products = cursor.fetchall()

# # Loop through and print each product
# for product in products:
#     print(product)

# # Save changes and close the connection
# conn.commit()
# conn.close()

 



import sqlite3

# Connect to database (creates file if it doesn’t exist)
conn = sqlite3.connect("new.db")

# Create a cursor (used to run SQL commands)
cursor = conn.cursor()


command1 = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age  INTEGER
    )
"""

cursor.execute(command1)

# CRUD operations

# (C)CREATE --> Insert data 

cursor.execute("INSERT INTO users(name,age) VALUES (?,?)",("Ajay",10))
cursor.execute("INSERT INTO users(name,age) VALUES (?,?)",("Ravi",9))
conn.commit()


# (R) READ --> Select data 


cursor.execute("SELECT * FROM users")
rows= cursor.fetchall()
for row in rows:
    print(row)


# (U) UPDATE --> Modify Data

cursor.execute("UPDATE users SET age = ? WHERE name = ?",(19,"Ravi"))
conn.commit()


# (D) DELETE --> Remove Data

cursor.execute("DELETE FROM users WHERE name =? ",("Ajay",))
cursor.execute("DELETE FROM users WHERE name =? ",("Ravi",))
conn.commit()


cursor.execute("SELECT * FROM users")
rows= cursor.fetchall()
for row in rows:
    print(row)


conn.close()