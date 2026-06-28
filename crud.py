from sqlalchemy.orm import Session

import models
import schemas


def create_patient(db: Session, patient: schemas.PatientCreate):
    new_patient = models.Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def get_patients(db: Session):
    return db.query(models.Patient).all()


def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_patient_by_phone(db: Session, phone: str):
    return db.query(models.Patient).filter(models.Patient.phone == phone).first()


def get_patients_by_doctor(db: Session, doctor: str):
    return db.query(models.Patient).filter(models.Patient.doctor == doctor).all()


def update_patient(db: Session, patient_id: int, patient_update: schemas.PatientUpdate):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None

    update_data = patient_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None

    db.delete(db_patient)
    db.commit()
    return db_patient