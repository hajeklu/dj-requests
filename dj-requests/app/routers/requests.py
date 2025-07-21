from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import RequestCreate, RequestOut
from app.db import get_db, Request
from typing import List

router = APIRouter(prefix="/requests", tags=["requests"])

@router.post("/", response_model=RequestOut, status_code=status.HTTP_201_CREATED)
async def create_request(request: RequestCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new song request.
    """
    new_request = Request(content=request.content)
    db.add(new_request)
    await db.commit()
    await db.refresh(new_request)
    return new_request

@router.get("/", response_model=List[RequestOut])
async def list_requests(db: AsyncSession = Depends(get_db)):
    """
    List all song requests.
    """
    result = await db.execute(Request.__table__.select())
    return result.scalars().all()

@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_request(request_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a song request by ID.
    """
    result = await db.execute(Request.__table__.select().where(Request.id == request_id))
    request = result.scalar_one_or_none()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    await db.delete(request)
    await db.commit() 