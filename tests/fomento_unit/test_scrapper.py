from datetime import date
from src.fomento_unit.scrapper import retrieve


class FakeResponse:
    def __init__(self, status: int, content: str):
        self.status = status
        self.content = content

    async def text(self):
        return self.content


class ClientSession:
    def __init__(self, response: FakeResponse):
        self._response = response

    async def get(self, url: str, **kwargs):
        return self._response


async def test_origin_site_is_unavailable():
    response = FakeResponse(502, """
        <h1>Site unavailable</h1>
    """)
    session = ClientSession(response)

    value = await retrieve(session, date(2023, 5, 1))

    assert value is None


async def test_origin_successful_response():
    with open("tests/data/sii_2022.html", "rt") as site_response:
        content = site_response.read()

        response = FakeResponse(200, content)
        session = ClientSession(response)

        value = await retrieve(session, date(2022, 5, 1))

        assert value == "32.196,69"
