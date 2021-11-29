"""
Тестирование API


"""


import pytest

from main import init_app


@pytest.fixture
async def client(aiohttp_client):
    """Запуск приложения для тестирования"""
    app = await init_app()
    return await aiohttp_client(app)
