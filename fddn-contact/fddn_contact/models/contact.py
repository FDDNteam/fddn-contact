from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    Text,
    ForeignKey,
)

from .meta import Base


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(Unicode(50))


class ContactInfoItem(Base):
    __tablename__ = 'contact_info_item'
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)
    key = Column(Unicode(20))
    value = Column(Text)
    index = Column(Integer)


Index('contact_info_item_contact_id_idx', ContactInfoItem.contact_id)
Index('contact_user_id_idx', Contact.user_id, unique=True)
