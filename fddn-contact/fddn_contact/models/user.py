from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
)

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))
    password = Column(Unicode(80))


Index('user_name_idx', User.name, unique=True)
