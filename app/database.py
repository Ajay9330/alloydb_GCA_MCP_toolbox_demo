import os
import sqlalchemy
from google.cloud.alloydbconnector import Connector
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Optional

# global connector instance, will be initialized in main.py
connector: Optional[Connector] = None

# function to return a database connection object
def getconn() -> sqlalchemy.engine.base.Engine:
    if connector is None:
        raise RuntimeError("Database connector not initialized")
    conn = connector.connect(
        os.environ["INSTANCE_CONNECTION_NAME"],
        "pg8000",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        db=os.environ["DB_NAME"],
        ip_type="PUBLIC",
    )
    return conn

# create a SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
