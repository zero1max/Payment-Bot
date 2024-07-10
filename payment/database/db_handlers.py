import sqlite3
from dataclasses import dataclass, field

@dataclass
class Database:
    connect: sqlite3.Connection = field(init=False, default=None)
    cursor: sqlite3.Cursor = field(init=False, default=None)

    def __post_init__(self):
        self.connect = sqlite3.connect('product.db')
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            description TEXT NOT NULL,
            image TEXT NOT NULL
        )''')
        self.connect.commit()

    def add_products(self, name, price, description, image):
        self.cursor.execute("INSERT INTO products (name, price, description, image) VALUES (?, ?, ?, ?)", (name, price, description, image))
        self.connect.commit()

    def select_products(self):
        self.cursor.execute("SELECT * FROM products") 
        return self.cursor.fetchall()

    def select_product(self, name):
        self.cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        return self.cursor.fetchone()
    
    def delete_one(self, name, value):
        self.cursor.execute(f"DELETE FROM products WHERE {name}=?", (value,))
        self.connect.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()
