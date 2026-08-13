from fastapi import APIRouter, Depends
from ..schemas.user import UserCreate, UserLogin, RefreshToken
from ..core.database import session_dependency
from ..services.users import register_user

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/register')
async def register(user_data:UserCreate, db:session_dependency):
    return await register_user(user_data, db)

@auth_router.post('/login')
async def login(user:UserLogin):
    pass

@auth_router.post('/refresh')
async def refresh(refresh_token:RefreshToken):
    pass

@auth_router.post('/logout')
async def logout(refresh_token:RefreshToken):
    pass
