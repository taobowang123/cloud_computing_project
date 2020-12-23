from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, ForeignKey, DateTime, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the base class.
Base = declarative_base()

# Define the class
class Events(Base):
    # The name of table.
    __tablename__ = "Events"
    # The structure of the table.
    id = Column(Integer, primary_key=True, autoincrement=False)
    event = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    important_rank = Column(Integer, nullable=True)
    address = Column(String(50), nullable=True)
    note = Column(String(50), nullable=True)

# Define the Bike class
class time_booking(Base):
    # The name of table.
    __tablename__ = "time_booking"
    # The structure of the table.
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(Integer) # foreign key problem
    status = Column(String(50), nullable=False)
    bike_stands = Column(Integer, nullable=False)
    available_bike_stands = Column(Integer, nullable=False)
    available_bikes = Column(Integer, nullable=False)
    last_update = Column(DateTime, nullable=False)

# Init the database connection.
# For the local database test.
# engine = create_engine('mysql+pymysql://root:hanpeisong@localhost:3306/dbbikes')
# For the RDS
engine = create_engine('mysql+pymysql://root:127.0.0.1:3306/toDo')

# Create the type of DBSession.
Session = sessionmaker(bind=engine)

# Create the session object.
session = Session()

