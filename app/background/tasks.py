from fastapi import BackgroundTasks
from app.services.notification_service import send_notification

def notify_user_background(
    background_tasks: BackgroundTasks, user_id: int, message: str, notification_type: str = "system"
):
    """
    Schedule a notification to be sent in the background.
    This ensures main requests don’t wait for slow I/O.
    """
    background_tasks.add_task(send_notification, user_id, message, notification_type)
