import logging
import sys
import os
from datetime import datetime

def setup_logger(name: str = "AgainBuilders"):
    """Configure and return a logger with safe directory creation."""

    # Ensure logs directory exists
    log_dir = "app/logs"
    os.makedirs(log_dir, exist_ok=True)  # <-- This prevents FileNotFoundError

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)

        # File handler (creates one log file per day per module)
        log_filename = os.path.join(log_dir, f"{name}_{datetime.now().date()}.log")
        file_handler = logging.FileHandler(log_filename)

        # Formatting
        formatter = logging.Formatter(
            fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Attach handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

