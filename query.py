import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band='Lions of the IDE'")
all = cursor.fetchall()
# print(all)
cursor.execute("SELECT band, city FROM events where city='Clone City'")
rows = cursor.fetchall()
print(rows)
try: 
    new_rows = [
    ('Cats', 'Cat city', '5.6.2025'),
    ('Hens', 'Hens city', '5.6.2025')]
   
    cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
    # Commit the transaction
    connection.commit()
except sqlite3.Error as e:
    connection.rollback()
    print("Transaction rolled back:", e)
finally:
    connection.close()



