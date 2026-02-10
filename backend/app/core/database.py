from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGODB_URI)
db = client[settings.DB_NAME]

def get_db():
    return db
