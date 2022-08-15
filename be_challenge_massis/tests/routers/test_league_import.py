from ...models.league import League
from ...models.team import Team


def test_should_import_league(client, postgres):
    response = client.post("/import-league", json={"league_code": "PL"})

    with postgres().session() as session:
        assert session.query(League).count() == 1
    assert response.status_code == 201
    assert response.json() == {"message": "League imported successfully"}


def test_should_import_teams(client, postgres):
    response = client.post("/import-league", json={"league_code": "PL"})

    with postgres().session() as session:
        assert session.query(Team).count() == 20
    assert response.status_code == 201
    assert response.json() == {"message": "League imported successfully"}


def test_should_not_import_league_with_invalid_code(client, postgres):
    response = client.post("/import-league", json={"league_code": "XX"})

    with postgres().session() as session:
        assert session.query(League).count() == 0
    assert response.status_code == 404
    assert response.json() == {"detail": "Impossible to get this league"}


def test_should_not_import_league_with_existing_code(client, postgres):
    client.post("/import-league", json={"league_code": "PL"})

    response = client.post("/import-league", json={"league_code": "PL"})

    with postgres().session() as session:
        assert session.query(League).count() == 1
    assert response.status_code == 409
    assert response.json() == {"detail": "This League was already imported"}
