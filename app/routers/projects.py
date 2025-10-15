from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.project import Project
from app.core.database import get_db
from typing import List
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services.project_service import (
    get_all_projects,
    get_project_by_id,
    create_project,
    update_project,
    delete_project
)

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model= List[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)

@router.post("/", response_model=ProjectResponse)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db, project)

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project_info(project_id: int, update_data: ProjectUpdate, db: Session = Depends(get_db)):
    updated = update_project(db, project_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated

@router.delete("/{project_id}")
def remove_project(project_id: int, db: Session = Depends(get_db)):
    success = delete_project(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
