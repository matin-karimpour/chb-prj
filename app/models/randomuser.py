from sqlalchemy import (
	Table,
    Column,
    Integer,
	String, 
	Boolean, 
	UniqueConstraint, 
	PrimaryKeyConstraint

)

import jwt
import bcrypt

from db_initializer import Base, engine
import utils
import settings

class RandomUser(Base):
    __tablename__ = "chb"
    email = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    dob_age = Column(Integer, nullable=False,)
    login_password = Column(String(250), nullable=False)
    name_first = Column(String(225), nullable=False)
    name_last = Column(String(225), nullable=False)
    login_username = Column(String(225), nullable=False)
    location_country = Column(String(225), nullable=False)
    location_city = Column(String(225), nullable=False)

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.name_first+ " " + self.name_last)
