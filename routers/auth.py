from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserLogin, RefreshToken

router = APIRouter(prefix='/auth')

@router.post('/register')
async def register(user_data:UserCreate):
    pass

@router.post('/login')
async def login(user:UserLogin):
    pass

@router.post('/refresh')
async def refresh(refresh_token:RefreshToken):
    pass

@router.post('/logout')
async def logout(refresh_token:RefreshToken):
    pass
