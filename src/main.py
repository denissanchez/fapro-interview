import os
from aiohttp import web
from routes import routes
from tasks import startup, shutdown


async def make_app():
    app = web.Application()

    await startup.set_startup_tasks(app)
    await shutdown.set_shutdown_tasks(app)

    app.add_routes(routes)

    return app


if __name__ == "__main__":
    web.run_app(make_app(), port=os.environ.get('PORT', 8080))
