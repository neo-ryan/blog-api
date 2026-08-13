from ..schemas.user import UserCreate
from ..core.security import hash_password
from sqlalchemy.orm import Session
from ..core.repository import add_user, check_email
from fastapi import HTTPException

async def register_user(user_data:UserCreate, db:Session):
    hashed = hash_password(user_data.password)
    user_dict = user_data.model_dump()
    user_dict['password'] = hashed.decode('utf-8')
    exists = check_email(user_dict, db)
    if exists != None:
        raise HTTPException(status_code=409)
    else:
        result = add_user(user_dict, db)
        return result
    