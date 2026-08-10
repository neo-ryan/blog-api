from schemas.user import UserCreate
from core.security import hash_password

async def register_user(user_data:UserCreate):
    hashed = hash_password(user_data.password)
    user_dict = user_data.model_dump()
    user_dict['password'] = hashed