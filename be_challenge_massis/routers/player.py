from fastapi import APIRouter, Depends

from ..services import PlayerService

from ..dependencies.services import get_player_service

router = APIRouter()


@router.get(
    "",
    status_code=200,
    responses={404: {"description": "This league code does not exist!"}},
)
def get_league_players(
    league: str,
    team: str = None,
    player_service: PlayerService = Depends(get_player_service),
):
    result = player_service.get_players_by_league_and_team(league, team)
    return {"players": result}
