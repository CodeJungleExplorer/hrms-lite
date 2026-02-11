from app.core.database import employees_collection
from app.utils.validators import conflict


def create_employee(data: dict):
    existing = employees_collection.find_one({
        "$or": [
            {"employee_id": data["employee_id"]},
            {"email": data["email"]}
        ]
    })

    if existing:
        return None

    employees_collection.insert_one(data)
    data.pop("_id", None)
    return data


def list_employees():
    return list(employees_collection.find({}, {"_id": 0}))


def delete_employee(employee_id: str):
    result = employees_collection.delete_one({"employee_id": employee_id})
    return result.deleted_count
