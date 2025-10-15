import importlib
import pkgutil
import logging
from fastapi import FastAPI, Depends, HTTPException, status
from app import routers
from app.routers.auth import oauth2_scheme
from app.core.security import decode_access_token
import traceback


# noinspection PyBroadException
def include_all_routers(app: FastAPI, package_name: str = "app.routers"):
    """
    Dynamically imports and includes all routers in the given package.
    Logs success/failure for each router.
    """
    try:
        package = importlib.import_module(package_name)
    except ImportError as e:
        print(f" Failed to import router package '{package_name}': {e}")
        return

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        full_module_name = f"{package_name}.{module_name}"
        try:
            module = importlib.import_module(full_module_name)
            router = getattr(module, "router", None)
            if router:
                app.include_router(router)
                print(f"Router loaded: {full_module_name}")
            else:
                print(f"No router found in {full_module_name}")
        except Exception:
            print(f"Error loading {full_module_name}")
            traceback.print_exc()
