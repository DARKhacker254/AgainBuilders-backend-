from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from app.models.user import User
from app.schemas.user import UserCreate
from app.background.tasks import notify_user_background

def create_user(db: Session, user_data: UserCreate, background_tasks: BackgroundTasks):
    new_user = User(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    notify_user_background(
        background_tasks,
        user_id=new_user.id,
        message=f"Welcome {new_user.full_name} to AgainBuilders!",
        notification_type="email"
    )
    return new_user
