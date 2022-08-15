from fastapi import FastAPI

from .routers import league_import, player, team

app = FastAPI()

app.include_router(league_import.router, tags=["league_import"], prefix="")
app.include_router(player.router, tags=["player"], prefix="/player")
app.include_router(team.router, tags=["team"], prefix="/team")
