# setup_db.py
from config import engine
from lib.models import Base

Base.metadata.create_all(engine)
print("Database tables created.")
