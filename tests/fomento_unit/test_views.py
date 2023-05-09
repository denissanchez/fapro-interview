from src.main import make_app


async def test_get_value(aiohttp_client):
    client = await aiohttp_client(await make_app())
    response = await client.get("/fomento_unit?date=05-05-2023")

    data = await response.json()

    assert response.status == 200
    assert data['ok']
    assert data['date'] == "05-05-2023"
    assert data['value'] == "35.903,96"
