from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "hrms_lite")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

employees_collection = db["employees"]
attendance_collection = db["attendance"]   # ✅ ADD THIS LINE
