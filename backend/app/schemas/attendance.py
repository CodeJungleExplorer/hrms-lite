from pydantic import BaseModel, Field
from typing import Literal

class AttendanceCreate(BaseModel):
    employee_id: str = Field(..., min_length=1)
    date: str  # YYYY-MM-DD
    status: Literal["Present", "Absent"]


class AttendanceResponse(BaseModel):
    employee_id: str
    date: str
    status: str
