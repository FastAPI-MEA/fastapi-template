from fastapi import APIRouter


router = APIRouter(prefix="/auth")


@router.get("/ok")
async def ok() -> str:
    return "ok"