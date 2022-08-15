def test_should_get_team_by_name(client, sqlite):
    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/team?name=Arsenal FC")

    assert response.status_code == 200
    assert response.json().get("players") == None
    assert response.json().get("coaches") == None


def test_should_get_team_with_players_and_coach(client, sqlite):
    client.post("/import-league", json={"league_code": "PL"})
    response = client.get("/team?name=Arsenal FC&players=true")

    assert response.status_code == 200
    assert response.json().get("players")
    assert response.json().get("coaches")
