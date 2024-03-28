from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Text

from sqlalchemy.orm import relationship

from sqlalchemy.sql.expression import text

from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

