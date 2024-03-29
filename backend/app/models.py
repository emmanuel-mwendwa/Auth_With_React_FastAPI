from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.sql.expression import text

from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

from datetime import datetime


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    leads = relationship("Lead", back_populates="owner")

class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    company = Column(String, index=True, default="")
    note = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="leads")