import pandas
from sqlalchemy import Column, Float,Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, realtionship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/household",
    echo = True)

Base = declarative_base()

class Purchase(Base):
    __tablename__ = 'purchases'
    __table_args__ = {'schema':'london'}
    
    order_id = Column(Integer, primary_key = True)
    property_id = Column(Integer)
    property_city = Column(String(length = 250))
    property_state = Column(String(length = 250))
    product_id = Column(Integer)
    property_category = Column(String(length = 250))
    quantity = Column(String(length = 250))
    product_price = Column(Float)
    order_total = Column(Float)


    def __repr__(self):
        return "<Productt({0},{1},{2},{3},{4},{5},{7},{8})>".format(
            self.order_id, self.property_id, self.property_city, self.property_state,self.product_id,self.property_category,self.quantity,self.product_price,self.order_total
        )

Base.metadata.create_all(engine)

filename = "london.csv"

df = pandas.read_csv(filename)
df.to_sql(con = engine, name=Purchase.__tablename__, if_exists='append', index = False)


session_maker = sessionmaker()
session_maker.configure(bind = engine)
session = session_maker()

results = session.query(Purchase).limit(10).all()

for r in results:
    print(r)

