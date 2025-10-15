# app/workers/celery_worker.py
from celery import Celery

celery_app = Celery(
    "AgainBuilders",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def send_email_task(email: str):
    print(f"Sending email to {email}")
