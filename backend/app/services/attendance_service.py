from app.core.database import get_db
from app.models.attendance import ATTENDANCE_COLLECTION

def get_attendance_collection():
    db = get_db()
    return db[ATTENDANCE_COLLECTION]


def mark_attendance(attendance_data: dict):
    collection = get_attendance_collection()

    existing = collection.find_one({
        "employee_id": attendance_data["employee_id"],
        "date": attendance_data["date"]
    })

    if existing:
        return None

    collection.insert_one(attendance_data)
    return attendance_data


def get_attendance_by_employee(employee_id: str, on_date: str | None = None):
    collection = get_attendance_collection()

    query = {"employee_id": employee_id}
    if on_date:
        query["date"] = on_date

    return list(collection.find(query, {"_id": 0}))
