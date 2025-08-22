# CRUD Operations :- Implement Create, Read, Update, Delete operations for database records

import sqlite3

# Connect to database (creates file if it doesn’t exist)
conn = sqlite3.connect("inventory.db")

# Create a cursor (used to run SQL commands)
cursor = conn.cursor()

# CRUD operations

# (C)CREATE --> Insert data 

# Insert multiple categories
categories = [
    ("Electronics",),
    ("Furniture",),
    ("Clothing",),
    ("Books",)
]
cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

# Insert multiple products (linked to categories by category_id)
products = [
    ("Laptop", 10, 999.99, 1),   # (name, quantity, price, category_id)
    ("Chair", 20, 49.99, 2),
    ("T-Shirt", 50, 19.99, 3),
    ("Novel", 15, 12.99, 4)
]

cursor.executemany("INSERT INTO products (name, quantity, price, category_id) VALUES (?, ?, ?, ?)", products)

conn.commit()

##### (R) READ --> Select data 

# Read back categories
cursor.execute("SELECT * FROM categories")
print("Categories:")
for row in cursor.fetchall():
    print(row)

# Read back products
cursor.execute("SELECT * FROM products")
print("\nProducts:")
for row in cursor.fetchall():
    print(row)


# (U) UPDATE --> Modify Data

cursor.execute("UPDATE products SET quantity = ? WHERE id = ?",(222,2))
conn.commit()


# (D) DELETE --> Remove Data

cursor.execute("DELETE FROM products WHERE id =? ",(1,))
conn.commit()

print("After performing other crud opearations")
cursor.execute("SELECT * FROM products")
rows= cursor.fetchall()
for row in rows:
    print(row)


conn.close()