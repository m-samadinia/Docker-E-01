from . import SERVER_NAME, VERSION
from fastapi import FastAPI

app = FastAPI(title=SERVER_NAME, version=VERSION)
