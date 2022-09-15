from fastapi import APIRouter

from auth.api import router as auth
# add app routes like so:
# from app_name.api import router as app_name


router = APIRouter()
router.include_router(auth)
# router.include_router(app_name)