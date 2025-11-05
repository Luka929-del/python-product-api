import sqlite3

class Product:
    def __init__(self, name, category, price, id=None):
        self.name = name
        self.category = category
        self.price = price
        self.id = id

    def create(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Product (name, Category, Price) VALUES (?, ?, ?)",
            (self.name, self.category, self.price)
        )
        conn.commit()
        conn.close()

    @classmethod
    def read(cls, id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product WHERE id=?", (id,))
        data = cursor.fetchone()
        conn.close()
        if data:
            return Product(data[1], data[2], data[3], data[0])
        return None

    @classmethod
    def read_all(cls):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product")
        datas = cursor.fetchall()
        conn.close()

        product_list = []
        for data in datas:
            product_list.append(Product(data[1], data[2], data[3], data[0]))
        return product_list

    @classmethod
    def delete(cls, id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Product WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def update(self):
        if self.id is None:
            raise ValueError("Product ID is required for update")
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Product SET name=?, Category=?, Price=? WHERE id=?",
            (self.name, self.category, self.price, self.id)
        )
        conn.commit()
        conn.close()


