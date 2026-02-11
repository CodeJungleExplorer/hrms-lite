from fastapi import HTTPException
import traceback

from fastapi import APIRouter, HTTPException, status
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import (
    create_employee,
    list_employees,
    delete_employee
)
from app.utils.validators import not_found, conflict


router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def add_employee(employee: EmployeeCreate):
    result = create_employee(employee.dict())

    if not result:
        conflict("Employee with same ID or email already exists")


    return result


@router.get("/")
def get_employees():
    try:
        employees = list(employees_collection.find())
        return employees
    except Exception as e:
        print("EMPLOYEES ERROR:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))



@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_employee(employee_id: str):
    deleted = delete_employee(employee_id)

    if deleted == 0:
       not_found("Employee not found")

