import sqlalchemy as db

engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect() #proxy for true python database api connection

metadata = db.MetaData()

movies = db.Table('Movies', metadata, autoload = True, autoload_with = engine)

query = db.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall() #interact with it
print(result_set[:2])

query = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

query_object = movies.insert().values(Title="Psycho",Director="Alfred Hitchcock", Year = "1960")

connection.execute(query_object)
query = db.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall() #interact with it
print(result_set)
