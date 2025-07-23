from sqlalchemy import Column, String, ForeignKey, Numeric, Date, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    rating = Column(Numeric(2, 1))

    rooms = relationship("Room", back_populates="hotel")

class RoomType(Base):
    __tablename__ = "room_types"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)

class Room(Base):
    __tablename__ = "rooms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hotel_id = Column(UUID(as_uuid=True), ForeignKey("hotels.id"), nullable=False)
    room_number = Column(String, nullable=False)
    price_per_night = Column(Numeric(10, 2), nullable=False)
    room_type_id = Column(UUID(as_uuid=True), ForeignKey("room_types.id"))

    hotel = relationship("Hotel", back_populates="rooms")
    room_type = relationship("RoomType")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    address = Column(String, nullable=True)
    age = Column(Integer, nullable=True)

    bookings = relationship("Booking", back_populates="customer")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    room_id = Column(UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=False)
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)

    customer = relationship("Customer", back_populates="bookings")
    room = relationship("Room")
