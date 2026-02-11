from app.core.database import attendance_collection
from datetime import date
from app.utils.validators import conflict


def mark_attendance(data: dict):
    # Prevent duplicate attendance for same employee & date
    existing = attendance_collection.find_one({
        "employee_id": data["employee_id"],
        "date": data["date"]
    })

    if existing:
        return None

    attendance_collection.insert_one(data)
    data.pop("_id", None)
    return data


def get_attendance_by_employee(employee_id: str, date_filter: str | None = None):
    query = {"employee_id": employee_id}

    if date_filter:
        query["date"] = date_filter

    records = list(attendance_collection.find(query, {"_id": 0}))
    return records


def list_attendance():
    records = list(attendance_collection.find({}, {"_id": 0}))
    return records
