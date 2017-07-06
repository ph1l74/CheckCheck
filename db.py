from sqlalchemy import Column, DateTime, String, Integer, func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reciept(Base):
    __tablename__ = "reciept"
    id_number = Column(Integer, primary_key=True)
    id = Column(String)
    #date_payed = Column(DateTime)
    date_added = Column(DateTime, default=func.now())

    def add(self):
        s = session()
        s.add(self)
        s.commit()

engine = create_engine('sqlite:///db.sqlite')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
