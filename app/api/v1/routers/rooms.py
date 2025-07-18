from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import uuid

from app import models, schemas
from app.database import SessionLocal
from app.dependencies import get_db

router = APIRouter()

@router.post("/rooms/", response_model=schemas.Room)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    db_room = models.Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/rooms/", response_model=List[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = db.query(models.Room).offset(skip).limit(limit).all()
    print(f"Found {len(rooms)} rooms in the database.")
    for room in rooms:
        print(f"Room ID: {room.id}, Room Number: {room.room_number}")
    return rooms

@router.get("/rooms/{room_id}", response_model=schemas.Room)
def read_room(room_id: uuid.UUID, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@router.put("/rooms/{room_id}", response_model=schemas.Room)
def update_room(room_id: uuid.UUID, room: schemas.RoomCreate, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    for key, value in room.model_dump().items():
        setattr(db_room, key, value)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.delete("/rooms/{room_id}", response_model=schemas.Room)
def delete_room(room_id: uuid.UUID, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(db_room)
    db.commit()
    return db_room
