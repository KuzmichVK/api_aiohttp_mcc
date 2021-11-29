"""
Асинхронное API для получения информации об МСС.
Версия: 10
Автор: Кузьмич Валентин


"""


import yaml
import asyncpg
import asyncio
from aiohttp import web
from typing import Dict, Union
from aiohttp_apispec import setup_aiohttp_apispec
from bin.views.routes import setup_routes
from bin.controllers.middlewares import middleware_to_log


async def init_app() -> web.Application:
    """Создание приложения"""
    with open('env.yaml') as file:
        config: Dict[str, Dict[str, Union[int, str]]] = yaml.safe_load(file)

    config_app: Dict[str, Union[int, str]] = config['config_app']

    config_db: Dict[str, str] = config['config_db']

    app: web.Application = web.Application(
        middlewares=[
            middleware_to_log
        ],
        client_max_size=config_app['client_max_size']
    )

    app['pool'] = await asyncpg.create_pool(
        user=config_db['user'],
        password=config_db['password'],
        database=config_db['database'],
        host=config_db['host']
    )

    app['host']: str = config_app['host']
    app['port']: str = config_app['port']

    setup_routes(app)

    setup_aiohttp_apispec(
        app=app,
        title="Documentation to calculator API",
        version="v1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
    )

    return app


def main():
    """Запуск приложения"""
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, host=app['host'], port=app['port'])
    return app


if __name__ == "__main__":
    main()
