from sqlalchemy.orm import Session
from ..models.users import User

def add_user(user_dict:dict, db:Session):
    new_user = User(**user_dict)
    exists = check_email(user_dict, db)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def check_email(user_dict:dict, db:Session):
    email = user_dict['email']
    return db.query(User).filter_by(email=email).first()
    
    
