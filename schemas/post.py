from pydantic import BaseModel, Field, ConfigDict

class Post(BaseModel):
    author_id:int
    title:str = Field(min_length=4, max_length=16)
    content:str = Field(max_length=150)
    published:bool
    
class PostOut(Post):
    model_config = ConfigDict(from_attributes=True)
    id:int