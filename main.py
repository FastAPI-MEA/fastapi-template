import logging

import uvicorn
from fastapi import FastAPI

from app.routes import router
from app.settings import settings
from app.db import db


app = FastAPI(title=settings.APP_TITLE)

app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    """
    Server configurations
    """
    uvicorn.run(
        app="main:app",
        host=settings.ALLOWED_HOST,
        debug=settings.DEBUG,
        port=settings.ALLOWED_PORT,
        reload=True,
        log_level=logging.INFO,
        use_colors=True,
    )