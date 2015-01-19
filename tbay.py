from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('postgresql://tatianajtylosky:tatianajtylosky@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#List of relations
#- Items to Bids = one to many
#- Items to Users = one to many
#- Users to Bids = one to many

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('user.id'),
                             nullable=False)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    bids = relationship("Bid", backref="users")
    items = relationship("Item", backref="users")

class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'),
                             nullable=False)


Base.metadata.create_all(engine)
