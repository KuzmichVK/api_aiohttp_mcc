"""
Функции для тестирования API


"""


from test_main import client  # noqa: F401
from tests.test_cases import cases
from tests.utils import for_post


async def test_post_table(client) -> None:  # noqa: F811
    """Тестирование POST запроса /table_reimport"""
    await for_post("post_table", "/table_reimport", "table", client)


async def test_get_table(client) -> None:  # noqa: F811
    """Тестирование GET запроса /table_info"""
    for case in cases['table_info']:
        if case['parameter'] is not None:
            response = await client.get(
                "/table_info",
                params={"table": case['parameter']}
                # data=data для POST
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']
        else:
            response = await client.get(
                "/table_info"
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']


async def test_post_calculator(client) -> None:  # noqa: F811
    """Тестирование POST запроса /calculator"""
    await for_post("post_calculator", "/calculator", None, client)
