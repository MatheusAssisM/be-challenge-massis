def test_should_import_league(client):
    response = client.post("/import-league", json={"league_code": "PL"})
    assert response.status_code == 200
    assert response.json() == {"message": "League imported successfully"}
