from ...helpers.tests import league_output, teams_output


def test_should_get_team_by_name(client, mocker):
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league",
        return_value=league_output.copy(),
    )
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league_teams",
        return_value=teams_output.copy(),
    )

    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/team?name=Arsenal FC")

    assert response.status_code == 200
    assert response.json()["name"] == "Arsenal FC"


def test_should_get_team_with_players_and_coach(client, mocker):
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league",
        return_value=league_output.copy(),
    )
    mocker.patch(
        "be_challenge_massis.services.FootballAPIService.get_league_teams",
        return_value=teams_output.copy(),
    )
    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/team?name=Arsenal FC&players=true")

    assert response.status_code == 200
    assert response.json().get("players")
    assert response.json().get("coaches")
