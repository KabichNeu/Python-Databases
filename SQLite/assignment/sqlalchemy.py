import sqlalchemy as db

engine = db.create_engine('sqlite://users-sqlite.db')

metadata = db.MetaData()

connection = engine.connect()

users = db.Table('Users', metadata,
    db.Column('user_id', db.Integer, primary_key = True),
    db.Column('first_name', db.Text),
    db.Column('last_name', db.Text),
    db.Column('email_address', db.Text))

metadata.create_all(engine)

insertion_query = users.insert().values([
    {"first_name": "", "last_name":"","email_address":""},
    {"first_name": "", "last_name":"","email_address":""},
    {"first_name": "", "last_name":"","email_address":""},
    {"first_name": "", "last_name":"","email_address":""},
])

connection.execute(insertion_query)
 
selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
