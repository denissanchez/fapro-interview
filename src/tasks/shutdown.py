from aiohttp import web
from aiohttp import ClientSession


async def _dispose_session(app: web.Application):
    session: ClientSession = app['session']
    await session.close()


async def set_shutdown_tasks(app: web.Application):
    app.on_shutdown.append(_dispose_session)
