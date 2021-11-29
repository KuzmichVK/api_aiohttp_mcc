"""
Вспомогательные функции для тестирования запросов


"""


import ujson

from tests.test_cases import cases


async def for_post(cases_key: str, post_url: str, param: str, client) -> None:  # noqa: F811, E501
    """По циклу делает POST запросы"""
    headers = {'Content-type': 'application/json'}

    for case in cases[cases_key]:
        if (case['parameter'] is not None) and \
                (case['json_request'] is not None):
            response = await client.post(
                post_url,
                params={param: case['parameter']},
                data=ujson.dumps(case['json_request']),
                headers=headers
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']
        elif (case['json_request'] is None) and (case['parameter'] is None):
            response = await client.post(
                post_url
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']
        elif case['parameter'] is not None:
            response = await client.post(
                post_url,
                params={param: case['parameter']}
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']
        elif case['json_request'] is not None:
            response = await client.post(
                post_url,
                data=ujson.dumps(case['json_request']),
                headers=headers
            )
            assert response.status == case['response_status']
            assert await response.json() == case['json_response']
        else:
            pass
