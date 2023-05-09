import asyncio
import re
from datetime import date
from typing import Union

from aiohttp import ClientSession
from bs4 import BeautifulSoup

MONTH_IDENTIFIER = [
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre',
]


async def _retrieve_site(session: ClientSession, year: int):
    try:
        res = await session.get(f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm", timeout=2)

        if res.status != 200:
            return None

        text = await res.text()
        return re.sub(r'\n+', '', text)
    except asyncio.TimeoutError:
        return None


def _retrieve_value(content: Union[str, None], target_date: date):
    soup = BeautifulSoup(content, "html.parser")

    table_id = f"mes_{MONTH_IDENTIFIER[target_date.month - 1]}"
    target_section = soup.find("div", id=table_id)
    target_table = target_section.find("table")
    specific_day = target_table.find("th", width="40", string=target_date.day)

    return specific_day.next_sibling.text


async def retrieve(session: ClientSession, target_date: date):
    site_content = await _retrieve_site(session, target_date.year)

    if site_content is None:
        return None

    value = _retrieve_value(site_content, target_date)
    return value
