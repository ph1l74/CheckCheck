from sqlalchemy import Column, DateTime, String, Integer, func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reciept(Base):
    __tablename__ = "reciept"
    id = Column(Integer, primary_key=True)
    number = Column(String)
    date_payed = Column(DateTime)
    date_added = Column(DateTime, default=func.now())

def reciept_add(id, number, date_payed, date_added):
    new_reciept = Reciept(id=id, number=number, date_payed= date_payed, date_added=date_added)
    s = session()
    s.add(new_reciept)
    s.commit()


engine = create_engine('sqlite:///db.sqlite')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
