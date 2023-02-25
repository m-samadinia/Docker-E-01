from fastapi import APIRouter

from app.main.routers import api

router = APIRouter()
router.include_router(api.router, prefix="/api")
