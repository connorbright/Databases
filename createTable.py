connection = sqlite3.connect("DatabaseFile.db")

cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS StudentInfo(
               StudentID INTEGER PRIMARY KEY,
               FirstName TEXT NOT NULL,
               LastName TEXT NOT NULL)
               ''')

connection.commit()
connection.close()
