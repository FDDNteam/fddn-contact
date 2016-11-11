from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String
)

from .meta import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (
            self.username, self.password)


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    ContactName = Column(String)
    ContactInfo = Column(Text)


Index('my_index', User.username, unique=True, mysql_length=255)
