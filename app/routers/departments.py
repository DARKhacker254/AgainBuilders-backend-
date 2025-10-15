from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.core.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    new_dept = Department(name=dept.name)
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

@router.get("/", response_model=list)
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()
