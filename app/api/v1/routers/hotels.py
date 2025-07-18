from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from app import models, schemas
from app.database import SessionLocal
from app.dependencies import get_db

router = APIRouter()

@router.post("/hotels/", response_model=schemas.Hotel)
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    db_hotel = models.Hotel(**hotel.model_dump())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@router.get("/hotels/", response_model=List[schemas.Hotel])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels = db.query(models.Hotel).offset(skip).limit(limit).all()
    return hotels

@router.get("/hotels/{hotel_id}", response_model=schemas.Hotel)
def read_hotel(hotel_id: uuid.UUID, db: Session = Depends(get_db)):
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel

@router.put("/hotels/{hotel_id}", response_model=schemas.Hotel)
def update_hotel(hotel_id: uuid.UUID, hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    for key, value in hotel.model_dump().items():
        setattr(db_hotel, key, value)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@router.delete("/hotels/{hotel_id}", response_model=schemas.Hotel)
def delete_hotel(hotel_id: uuid.UUID, db: Session = Depends(get_db)):
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    db.delete(db_hotel)
    db.commit()
    return db_hotel
