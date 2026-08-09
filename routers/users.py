from fastapi import APIRouter, Query, Depends
from core.database import session_dependency

router = APIRouter(prefix='/users')

@router.get('/me')
async def current_user(token:str):
    pass
