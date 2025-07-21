from pydantic import BaseModel, Field

class RequestCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=255, description="Song request content")

class RequestOut(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True 