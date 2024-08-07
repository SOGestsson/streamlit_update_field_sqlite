
import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rio.db')
connection_string = f'sqlite:///{db_path}'

engine = create_engine(connection_string)

Base = declarative_base()

class RioItems(Base):
    __tablename__ = 'rio_items'
    id = Column(Integer, primary_key=True)
    buy_freq = Column(Integer, nullable = False)
    del_time = Column(Integer, nullable = False)
    innkaupum_haett = Column(Integer, nullable = False)


# Create a configured "Session" class
Session = sessionmaker(bind=engine)

