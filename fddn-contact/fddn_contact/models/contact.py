from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer)
    user_id = Column(Integer)
    ContactName = Column(string)

class ContactInfoItem(Base):
    pass:
