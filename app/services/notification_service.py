import logging
from datetime import datetime
from typing import Literal

logger = logging.getLogger("notifications")

def send_notification(user_id: int, message: str, notification_type: Literal["system", "email", "sms"] = "system"):
    """
    Send a notification to a user. Currently, logs the message.
    In production, this can dispatch to email, SMS, or push services.
    """
    timestamp = datetime.utcnow().isoformat()

    if notification_type == "email":
        # TODO: Integrate email delivery
        logger.info(f"[EMAIL] {timestamp} - User {user_id}: {message}")
    elif notification_type == "sms":
        # TODO: Integrate SMS provider (e.g., Twilio)
        logger.info(f"[SMS] {timestamp} - User {user_id}: {message}")
    else:
        logger.info(f"[SYSTEM] {timestamp} - User {user_id}: {message}")

    return {"user_id": user_id, "message": message, "type": notification_type, "timestamp": timestamp}
