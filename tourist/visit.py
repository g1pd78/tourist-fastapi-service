from fastapi import APIRouter, HTTPException, status
from places.destination import Tour, TourBasicInfo, TourInput, TourLocation, \
                               tours, tours_basic_info, tours_locations
from uuid import UUID, uuid1
from login.user import approved_users
from datetime import datetime 
from pydantic import BaseModel
from typing import List


router = APIRouter()

tour_references = set()

class Visit(BaseModel):
    id: UUID
    destination: List[TourBasicInfo]
    last_tour: datetime

class Booking(BaseModel):
    id: UUID
    destination: TourBasicInfo
    booking_date: datetime
    tourist_id: UUID


@router.post("/tourist/tour/booking/add")
def create_booking(tour: TourBasicInfo, touristId: UUID):
    if approved_users.get(touristId) == None:
        raise HTTPException(status_code=500, detail="details are missing")
    booking = Booking(id=uuid1(), destination=tour,
                      booking_date=datetime.now(), tourist_id=touristId)
    approved_users[touristId].tours.append(tour)
    approved_users[touristId].booked += 1
    tours[tour.id].idBooked = True
    tours[tour.id].visit += 1
    return booking  