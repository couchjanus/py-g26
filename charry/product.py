import sqlite3

db = 'product.db'

class Product:
    def __init__(self) -> None:
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM products")
            self.products = cursor.fetchall()
            
    def all(self) -> any:
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM products")
            return cursor.fetchall()
    def create(self, product):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            sql = "Insert Into products(name, price, description, picture) Values(?, ?, ?, ?)"
            cursor.execute(sql, product)
            con.commit()
            return cursor.lastrowid
        
        