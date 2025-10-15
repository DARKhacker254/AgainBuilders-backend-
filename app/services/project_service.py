from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def get_all_projects(db: Session):
    return db.query(Project).all()

def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project_data: ProjectCreate):
    new_project = Project(**project_data.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def update_project(db: Session, project_id: int, project_data: ProjectUpdate):
    project = get_project_by_id(db, project_id)
    if not project:
        return None
    for field, value in project_data.dict(exclude_unset=True).items():
        setattr(project, field, value)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = get_project_by_id(db, project_id)
    if project:
        db.delete(project)
        db.commit()
        return True
    return False
if __name__ == "__main__":
    print("✅ Project service module is working!")
