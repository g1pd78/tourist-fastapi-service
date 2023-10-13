from fastapi import APIRouter, status
from login.user import Signup, User, Tourist, pending_users, approved_users
from places.destination import Tour, TourBasicInfo, TourInput, TourLocation, \
                               tours, tours_basic_info, tours_locations
from fastapi.responses import JSONResponse
from uuid import uuid1
from fastapi.encoders import jsonable_encoder


router = APIRouter()

@router.get("/admin/tourists/list")
def list_all_tourists():
    return approved_users

@router.put("/admin/destination/update",
            status_code=status.HTTP_202_ACCEPTED)
def update_tour_destination(tour: Tour):
    try:
        tid = tour.id
        tours[tid] = tour
        tour_basic_info = TourBasicInfo(id=tid, name=tour.name, type=tour.type,
                                        amenities=tour.amenities, ratings=tour.ratings)
        tour_location = TourLocation(id=tid, name=tour.name, city=tour.city, country=tour.country,
                                     location=tour.location)
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        return {"message": "tour updated"}
    except:
        return {"message": "tour does not exist"}

@router.post("/admin/destination/add")
def add_tour_destination(input: TourInput):
    try:
        tid = uuid1()
        tour = Tour(id=tid, name=input.name,
                    city=input.city, country=input.country,
                    type=input.type, location=input.location,
                    amenities=input.amenities, feedbacks=list(),
                    rating=0.0, visits=0, isBookes=False)
        tour_basic_info = TourBasicInfo(id=tid, name=input.name,
                    type=input.type, amenities=input.amenities, rating=0.0)
        tour_location = TourLocation(id=tid, name=input.name,
                    city=input.city, country=input.country, location=input.location)
        tours[tid] = tour
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        tour_json = jsonable_encoder(tour)
        return JSONResponse(content=tour_json, status_code=status.HTTP_201_CREATED)
    except:
        return JSONResponse(content={"message": "invalid tour"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    