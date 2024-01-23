from pydantic import BaseModel, Field, EmailStr

class RandomUserSchema(BaseModel):
	id:int

class RandomUserLocationSchema(BaseModel):
	# age: int
	country: str
	# city: str