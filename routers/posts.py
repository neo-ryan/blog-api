from fastapi import APIRouter, Query

router = APIRouter(prefix='/posts')

@router.get('/')
async def get_posts(post_id:int = Query(default=None), author:str = Query(default=None, min_length=4)):
    pass

@router.post('/')
async def add_post():
    pass

@router.put('/{post_id}')
async def edit_post():
    pass

@router.delete('/{post_id}')
async def delete_post():
    pass