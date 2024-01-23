from pydantic import BaseModel, Field, EmailStr

class RandomUserSchema(BaseModel):
	id:int
