from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import router
from app.init_db import init_db, drop_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await drop_db()


app = FastAPI(lifespan=lifespan)

app.include_router(router)
