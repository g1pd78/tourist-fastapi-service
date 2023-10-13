from uuid import UUID, uuid1
from fastapi import APIRouter
from pydantic import BaseModel
from places.destination import Post

router = APIRouter()

class Assessment(BaseModel):
    id: UUID
    post: Post
    tour_id: UUID
    tourist_id: UUID