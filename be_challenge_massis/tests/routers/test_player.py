from ...models import Player, Team


def test_should_get_league_players(client, sqlite):
    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/player?league=PL")

    with sqlite().session() as session:
        db_count = session.query(Player).count()
    assert response.status_code == 200
    assert len(response.json()["players"]) == db_count


def test_should_get_league_players_by_team_name(client, sqlite):
    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/player?league=PL&team=Arsenal")

    with sqlite().session() as session:
        team_id = session.query(Team).filter(Team.name.like("%Arsenal%")).first().id
        db_count = session.query(Player).filter(Player.team_id == team_id).count()
    assert response.status_code == 200
    assert len(response.json()["players"]) == db_count
