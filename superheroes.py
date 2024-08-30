from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///dash.db', echo=True)
Base = declarative_base()

class MovieModel(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)  # Assuming date is stored as a string
    time = Column(String)  # Assuming time is stored as a string

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
