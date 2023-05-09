from datetime import date
from typing import Union

from aiohttp import web

from .rules.dates import get_date_or_default
from .scrapper import retrieve


async def detail(request: web.Request):
    _candidate: str = request.query.get('date', None)
    target: Union[date, None] = get_date_or_default(_candidate)

    if target is None:
        return web.json_response({
            'ok': False,
            'message': 'Please, try to enter a valid date.'
        }, status=400)

    value = await retrieve(request.app['session'], target)

    return web.json_response({
        'ok': value is not None,
        'value': value,
        'date': target.strftime('%d-%m-%Y')
    })
