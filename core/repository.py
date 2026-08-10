from sqlalchemy.orm import Session
from models.users import User
from schemas.user import UserCreate

async def add_user(user_data:UserCreate, db:Session):
    pass