from fastapi import FastAPI

from .routers import league

app = FastAPI()

app.include_router(league.router, tags=["league"], prefix="")
