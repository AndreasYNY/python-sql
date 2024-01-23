from fastapi import APIRouter

router = APIRouter()

from . import employee

router.include_router(employee.router)