from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(Text)


class ContactInfoItem(Base):
    __tablename__ = 'contact_info_item'
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    key = Column(Integer)
    value = Column(Text)
