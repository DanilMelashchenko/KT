from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import engine, get_db

# Створення таблиць
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student API with Docker",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Вітаємо у Student API!",
        "status": "running in Docker",
        "docs_url": "http://localhost/docs" # Змінив для Nginx
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email вже існує")
    
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/", response_model=List[schemas.StudentResponse])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Student).offset(skip).limit(limit).all()

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студента не знайдено")
    db.delete(student)
    db.commit()
    return {"message": "Студента видалено"}