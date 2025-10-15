from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger("uvicorn.error")

def setup_exception_handlers(app: FastAPI):
    """Attach custom global exception handlers to the app."""

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error(f"HTTP error: {exc.detail} (status: {exc.status_code})")
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail, "status": exc.status_code},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.warning(f"Validation error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"error": "Invalid input", "details": exc.errors()},
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.critical(f"Unhandled exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"error": "Something went wrong. Please try again later."},
        )

    logger.info("Exception handlers configured successfully")
