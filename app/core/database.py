# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

#  Step 1: Tell it what notebook (database) to use
DATABASE_URL = "sqlite:///./againbuilders.db"  # this makes a local file called againbuilders.db

#  Step 2: Create a little bridge between your app and that notebook
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#  Step 3: Make a session (a little helper that opens/closes the notebook safely)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#  Step 4: Create a Base — it’s like a page template for your tables
Base = declarative_base()

# Step 5: Helper for your routes — it opens a connection to the notebook
def get_db():
    db = SessionLocal()
    try:
        yield db  # “here, use the notebook for this request”
    finally:
        db.close()  # “okay, close the notebook when you’re done”

