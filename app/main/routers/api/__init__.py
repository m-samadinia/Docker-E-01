from fastapi import APIRouter

from app.main.routers.api import routes

router = APIRouter()
router.include_router(routes.router, prefix="/routes", tags=["Routes"])