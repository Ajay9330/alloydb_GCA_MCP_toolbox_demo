import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app import database
from app.database import engine, Base
from app.api.v1.routers import hotels, rooms, customers, bookings
from google.cloud.alloydbconnector import Connector
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Connecting to database...")
    with Connector() as connector:
        database.connector = connector
        logger.info("Database connection successful.")
        yield
    logger.info("Database connection closed.")

app = FastAPI(lifespan=lifespan)

app.include_router(hotels.router, prefix="/api/v1", tags=["hotels"])
app.include_router(rooms.router, prefix="/api/v1", tags=["rooms"])
app.include_router(customers.router, prefix="/api/v1", tags=["customers"])
app.include_router(bookings.router, prefix="/api/v1", tags=["bookings"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hotel Management API"}
