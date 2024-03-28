from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
import pyodbc


engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    
    id = Column(Integer, primary_key=True)

    
    oxygen = Column(Integer)

    
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password'%s')>" % (
                               self.date, self.time, self.oxygen)


Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(oxygen=89)

session.add(ed_user)
session.commit()

q = engine.execute("select * from User")
for r in q:
    print(r)
print (q)


