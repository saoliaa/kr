from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, Index=True)
    name = Column(String)
    email = Column(String, Index=True)
