from fastapi import APIRouter, status, BackgroundTasks
from typing import List
from pydantic import BaseModel
from uuid import UUID, uuid1
from datetime import datetime
from places.destination import TourBasicInfo


router = APIRouter()

pending_users = dict()
approved_users = dict()

class Signup(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    birthday: datetime

class User(BaseModel):
    id: UUID
    username: str
    password: str

class Tourist(BaseModel):
    id: UUID
    login: User
    date_signed: datetime
    booked: int
    tours: List[TourBasicInfo]
