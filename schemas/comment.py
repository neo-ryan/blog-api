from pydantic import BaseModel, Field, ConfigDict

class Comment(BaseModel):
    content:str = Field(max_length=150)
    author:str 
    
class CommentOut(Comment):
    model_config = ConfigDict(from_attributes=True)
    id:int