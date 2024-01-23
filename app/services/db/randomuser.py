from sqlalchemy.orm import Session
from sqlalchemy import select

from models.randomuser import RandomUser
from schemas.users import CreateUserSchema





def get_random_user_by_id(session:Session, id:int):
	return session.query(RandomUser).filter(RandomUser.id == id).one()