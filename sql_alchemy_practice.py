from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



def create_session(engine):
  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  return session

def engine():
  engine = create_engine('sqlite:///delete_me.db', echo=True)
  return engine
  
def create_base():
  Base = declarative_base()
  return Base
  

Base = create_base()
    
class Candidate(Base):
  __tablename__ = 'candidates'
  id = Column(Integer, primary_key = True)
  email = Column(String)
  first = Column(String)
  
  def __repr__(self):
    return "<Candidate(email='%s', first='%s', last='%s', company='%s', title='%s' linkedin='%s', role='%s')>" % (self.name, self.first, self.last, self.company, self.title, self.linkedin, self.role)    
    







