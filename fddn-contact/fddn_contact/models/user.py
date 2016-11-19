from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    password = Column(Text)


Index('user_name_idx', User.name, unique=True)
