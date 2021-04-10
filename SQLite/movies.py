import sqlite3

connection = sqlite3.connect('movies.db')   #CREATE A DATABASE

cursor = connection.cursor()
 
# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
#     (Title TEXT, Director TEXT, Year INT)''')

#cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorses', 1976)")


famousFilms = [('Pulp Fiction','Quentin Tarantino', 1994),
('Back to the Future','Steven Spielberg', 1985),
('Moonrise Kingdom', 'Wes Anderson', 2012)]

cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)

# print(cursor.fetchall()) 

records = cursor.execute("SELECT * FROM Movies")
for record in records:
    print(record)

release_year = (1985,)

cursor.execute("SELECT * FROM MOVIES WHERE Year=?", release_year)
print(cursor.fetchall())
connection.commit()  #commit the changes 
connection.close()   #close the connection