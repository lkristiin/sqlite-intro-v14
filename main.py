import sqlite3
from pathlib import Path

folder = Path(_file_).resolve().parent
con = sqlite3.connect(folder / "app.db")

con.execute("""
CREATE TABLE IF NOT EXITS books (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    value INTEGER  
 )
 """)

 data = [
    ("Деревянный стул", "Дерево", 1850),
    ("Бронзовая статуя", "Металл", 1920),
    ("Деревянный сундук", "Дерево", 1905),
    ("Картина маслом", "Живопись", 1950),
    ("Деревянная шкатулка", "Дерево", 1890),
    ("Железный меч", "Металл", 1850),
    ("Глиняный кувшин", "Керамика", 1910),
    ("Каменная плита", "Камень", 1800),
]

count = con.execute("SELECT COUNT(*) FROM exhibits").fetchone()[0]

if count == 0:
    con.executemany(
        "INSERT INTO exhibits (name, category, value)"
        "VALUES (?, ?, ?)",
        data
    )
    con.commit()

print("Все записи:")
rows = con.execute("SELECT * FROM exhibits ORDER BY id").fetchall(

for row in rows:
    print(row)

print("\nВыбранная категория (Дерево):")
chosen_category = "Дерево"
rows = con.execute(
    "SELECT * FROM exhibits WHERE category = ?",
    (chosen_category,)
).fetchall()
for row in rows:
    print(row)

print("\nФильтр (год < 1900):")
limit = 1900
rows = con.execute(
    "SELECT * FROM exhibits WHERE value < ?",
    (limit,)
).fetchall()
for row in rows:
    print(row)

print("\nСортировка по году (ASC):")
rows = con.execute("SELECT * FROM exhibits ORDER BY value ASC, id ASC"
).fetchall()
for row in rows:
    print(row)

print("\nИзменение записи (id = 1):")
record_id = 1
new_value = 1860

con.execute(
    "UPDATE exhibits SET value = ? WHERE id = ?",
    (new_value, record_id)
)
con.commit()

print(con.execute(
    "SELECT * FROM exhibits WHERE id = ?",
    (record_id,)
).fetchone())

print("\nУдаление записи (id = 3):")
record_id = 3
con.execute(
    "DELETE FROM exhibits WHERE id = ?",
    (record_id,)
)
con.commit()

print("После удаления:")
for row in con.execute("SELECT * FROM exhibits ORDER BY id"):
    print(row)

con.close()
