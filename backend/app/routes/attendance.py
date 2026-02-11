from fastapi import APIRouter, status, Query
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.services.attendance_service import (
    mark_attendance,
    get_attendance_by_employee,
    list_attendance
)
from app.utils.validators import not_found, conflict

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post(
    "/",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED
)
def add_attendance(attendance: AttendanceCreate):
    result = mark_attendance(attendance.model_dump())

    if not result:
        conflict("Attendance already marked for this employee on this date")

    return result


# ✅ NEW: Dashboard / global attendance
@router.get("/", response_model=list[AttendanceResponse])
def get_all_attendance():
    return list_attendance()


# ✅ Existing: per-employee attendance
@router.get("/{employee_id}", response_model=list[AttendanceResponse])
def get_attendance(
    employee_id: str,
    date: str | None = Query(None)
):
    records = get_attendance_by_employee(employee_id, date)

    if not records:
        not_found("No attendance records found")

    return records
