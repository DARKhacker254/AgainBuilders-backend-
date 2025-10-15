import logging
import pkgutil
import importlib
from app import routers
from fastapi import FastAPI
from app.core.utils import include_all_routers
from app.core.database import Base, engine
from app.core.config import settings
from app.routers import auth, users, projects, departments
from app.core.errors import setup_exception_handlers
from app.core.loggers import setup_logger
from fastapi import FastAPI
from app.core.exceptions import setup_exception_handlers
from app.bootstrap import init_db
# assuming you have this module

# noinspection PyUnboundLocalVariable
logger = setup_logger("main")

app = FastAPI(title="AgainBuilders")

setup_exception_handlers(app)
include_all_routers(app)
# Include all routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(departments.router)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting AgainBuilders...")
    include_all_routers(app)
    logger.info("All routers loaded successfully.")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down AgainBuilders. Goodbye!")

@app.get("/")
def root():
    return {"message": "Welcome to AgainBuilders  — Phase 3.5 "}

