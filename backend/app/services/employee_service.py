from app.core.database import get_db
from app.models.employee import EMPLOYEE_COLLECTION

def get_employee_collection():
    db = get_db()
    return db[EMPLOYEE_COLLECTION]


def create_employee(employee_data: dict):
    collection = get_employee_collection()

    # Duplicate check (employee_id OR email)
    if collection.find_one({
        "$or": [
            {"employee_id": employee_data["employee_id"]},
            {"email": employee_data["email"]}
        ]
    }):
        return None

    collection.insert_one(employee_data)
    return employee_data


def list_employees():
    collection = get_employee_collection()
    employees = list(collection.find({}, {"_id": 0}))
    return employees


def delete_employee(employee_id: str):
    collection = get_employee_collection()
    result = collection.delete_one({"employee_id": employee_id})
    return result.deleted_count
