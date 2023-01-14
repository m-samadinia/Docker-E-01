from . import SERVER_NAME, VERSION
from fastapi import FastAPI
from .routers.api.routes import router

app = FastAPI(title=SERVER_NAME, version=VERSION)
app.include_router(router)
