from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime
import uuid

class RoomBase(BaseModel):
    room_number: str
    price_per_night: float

class RoomCreate(RoomBase):
    hotel_id: uuid.UUID

class Room(RoomBase):
    id: uuid.UUID
    hotel_id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)

class HotelBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    rating: Optional[float] = None

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    id: uuid.UUID
    rooms: List[Room] = []
    model_config = ConfigDict(from_attributes=True)

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)

class BookingBase(BaseModel):
    check_in_date: date
    check_out_date: date

class BookingCreate(BookingBase):
    customer_id: uuid.UUID
    room_id: uuid.UUID
    total_price: float

class Booking(BookingBase):
    id: uuid.UUID
    customer_id: uuid.UUID
    room_id: uuid.UUID
    total_price: float
    model_config = ConfigDict(from_attributes=True)
