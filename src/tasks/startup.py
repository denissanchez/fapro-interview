from aiohttp import web
from aiohttp import ClientSession


async def _create_session(app: web.Application):
    app['session'] = ClientSession()


async def set_startup_tasks(app: web.Application):
    app.on_startup.append(_create_session)
