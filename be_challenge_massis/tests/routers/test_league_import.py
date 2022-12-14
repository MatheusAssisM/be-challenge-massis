from ...helpers.tests import league_output, teams_output
from ...models.league import League
from ...models.team import Team


def test_should_import_league(client, sqlite, mocker):
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league",
        return_value=league_output.copy(),
    )
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league_teams",
        return_value=teams_output.copy(),
    )
    response = client.post("/import-league", json={"league_code": "PL"})

    with sqlite().session() as session:
        assert session.query(League).count() == 1
    assert response.status_code == 201
    assert response.json() == {"message": "League data imported successfully!"}


def test_should_import_teams(client, sqlite, mocker):
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league",
        return_value=league_output.copy(),
    )
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league_teams",
        return_value=teams_output.copy(),
    )
    response = client.post("/import-league", json={"league_code": "PL"})

    with sqlite().session() as session:
        assert session.query(Team).count() == 20
    assert response.status_code == 201
    assert response.json() == {"message": "League data imported successfully!"}


def test_should_not_import_league_with_invalid_code(client, sqlite):
    response = client.post("/import-league", json={"league_code": "XX"})

    with sqlite().session() as session:
        assert session.query(League).count() == 0
    assert response.status_code == 404
    assert response.json() == {"detail": "Impossible to get this league"}


def test_should_not_import_league_with_existing_code(client, sqlite, mocker):
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league",
        return_value=league_output.copy(),
    )
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league_teams",
        return_value=teams_output.copy(),
    )
    client.post("/import-league", json={"league_code": "PL"})

    response = client.post("/import-league", json={"league_code": "PL"})

    with sqlite().session() as session:
        assert session.query(League).count() == 1
    assert response.status_code == 409
    assert response.json() == {"detail": "League data is already up to date!"}
