"""
В данном файле описаны запросы к API


"""

from aiohttp import web

from bin.views.api_interactions import (
    get_table,
    post_table,
    post_calculator
)


def setup_routes(app: web.Application) -> None:
    """Добавление в приложение путей для запросов"""
    app.router.add_get(
        '/table_info',
        get_table,
        allow_head=False
    )
    app.router.add_post(
        '/table_reimport',
        post_table
    )
    app.router.add_post(
        '/calculator',
        post_calculator
    )
