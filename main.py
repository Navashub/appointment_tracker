from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Appointment Tracker API")


@app.post("/patients/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    existing = crud.get_patient_by_phone(db, patient.phone)
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    return crud.create_patient(db, patient)


@app.get("/patients/", response_model=list[schemas.PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)


@app.get("/patients/doctor/{doctor_name}", response_model=list[schemas.PatientResponse])
def get_patients_by_doctor(doctor_name: str, db: Session = Depends(get_db)):
    return crud.get_patients_by_doctor(db, doctor_name)


@app.get("/patients/{patient_id}", response_model=schemas.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


@app.put("/patients/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(
    patient_id: int, patient_update: schemas.PatientUpdate, db: Session = Depends(get_db)
):
    db_patient = crud.update_patient(db, patient_id, patient_update)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.delete_patient(db, patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Appointment deleted successfully"}