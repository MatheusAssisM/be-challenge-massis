from fastapi import APIRouter, Depends

from ..dependencies.services import get_team_service
from ..services import TeamService

router = APIRouter()


@router.get(
    "",
    status_code=200,
    responses={404: {"description": "This team does not exist!"}},
)
def get_team_by_name(
    name: str,
    players: bool = False,
    team_service: TeamService = Depends(get_team_service),
):
    result = team_service.get_team_by_name(name, players)
    return result
