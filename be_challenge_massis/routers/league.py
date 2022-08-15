from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from ..schemas.league import ImportLeague
from ..services.league_import import LeagueImportService
from ..dependencies.services import get_league_service

router = APIRouter()


@router.post(
    "/import-league",
    status_code=201,
    responses={409: {"description": "This League was already imported"}},
)
def import_league(
    data: ImportLeague,
    league_service: LeagueImportService = Depends(get_league_service),
):
    data = jsonable_encoder(data)
    result = league_service.import_league(data["league_code"])
    return {"message": result}
