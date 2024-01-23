from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import and_
from models.randomuser import RandomUser
from schemas.users import CreateUserSchema





def get_random_user_by_id(session:Session, id:int):
	return session.query(RandomUser).filter(RandomUser.id == id).one()

def get_random_user_by_location(session:Session, country:str):
	return session.query(RandomUser).filter(RandomUser.location_country == country).all()
											# filter(RandomUser.location_city==city).\
											# filter(RandomUser.dob_age==age).all()