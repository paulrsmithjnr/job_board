from fastapi import APIRouter

from api.version1 import route_users

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/user", tags=["users"])