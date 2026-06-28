from typing import Optional

from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    phone: str
    doctor: str
    appointment_date: str
    status: Optional[str] = "scheduled"


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    doctor: Optional[str] = None
    appointment_date: Optional[str] = None
    status: Optional[str] = None


class PatientResponse(BaseModel):
    id: int
    name: str
    phone: str
    doctor: str
    appointment_date: str
    status: str

    class Config:
        from_attributes = True