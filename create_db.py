import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Product(id INTEGER PRIMARY KEY, name TEXT, Category TEXT, Price Real)")
conn.commit()
conn.close()