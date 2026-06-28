from sqlalchemy import Column, Integer, String

from database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    doctor = Column(String, nullable=False)
    appointment_date = Column(String, nullable=False)
    status = Column(String, default="scheduled")