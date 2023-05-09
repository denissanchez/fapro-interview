from aiohttp import web

from typing import List

from fomento_unit.views import detail


__all__ = ['routes']


routes: List[web.RouteDef] = [
    web.get("/fomento_unit", detail)
]
