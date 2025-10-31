import sqlite3

connection = sqlite3.connect("FruitBasket.db", timeout=5)
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS Fruits;")

cur.execute("""
CREATE TABLE Fruits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    color TEXT
);
""")

cur.execute("INSERT INTO Fruits (name, color) VALUES ('Яблуко', 'Червоне');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Банан', 'Жовтий');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Апельсин', 'Помаранчевий');")
connection.commit()

cur.execute("UPDATE Fruits SET color = 'Зелене' WHERE name = 'Яблуко';")
connection.commit()

cur.execute("SELECT id, name, color FROM Fruits WHERE color = 'Жовтий';")
yellow = cur.fetchall()
print("ЖОВТІ:", yellow)

cur.execute("SELECT id, name, color FROM Fruits;")
all_fruits = cur.fetchall()
print("ВСІ:", all_fruits)

connection.close()
