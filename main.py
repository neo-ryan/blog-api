from fastapi import FastAPI
from .routers.auth import auth_router
from .models.users import User
from .models.comments import Comment
from .models.posts import Post

app = FastAPI(
    title='Blog API'
)

app.include_router(auth_router)