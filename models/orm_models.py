
import os
import urllib.parse
import pyodbc
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker


# Correct the params line using urllib.parse.quote_plus
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.80.61.10;DATABASE=rio;UID=riouser;PWD=phU$E5ib!3Zanl*0s$t5;TrustServerCertificate=yes;")

# Create the engine
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, fast_executemany=True, connect_args={'connect_timeout': 10}, echo=False)

# Define the base class for models
Base = declarative_base()

class RioItems(Base):
    __tablename__ = 'rio_item_editables'
    __table_args__ = {'schema': 'prod'}  # Specify the schema

    id = Column(Integer, primary_key=True)
    item_number = Column(String, nullable = False)
    description = Column(String, nullable = False)
    buy_freq = Column(Integer, nullable = False)
    del_time = Column(Integer, nullable = False)
    innkaupum_haett = Column(Integer, nullable = False)


# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create an instance of the session
session = Session()

# Perform the query using the session instance
query = session.query(RioItems).filter(RioItems.innkaupum_haett == 0)

# Example: Fetch all matching records
results = query.all()

# Print the results
for item in results:
    print(f"id: {item.id}, Item Number: {item.item_number}, Description: {item.description}, Buy_Freq:{item.buy_freq}")

