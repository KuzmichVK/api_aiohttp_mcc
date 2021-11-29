"""
Функции для обработки запросов


"""


import json
from aiohttp import web
from http import HTTPStatus
from typing import Dict, List, Union


async def request_table_name(request: web.Request, attr: str) -> \
        (str, Dict[str, str], int):
    """
    Пробуем получить название таблицы,
    в случае неудачи пишем лог и отправлям ответ.
    """
    try:
        attr_name: str = request.query[attr]
    except KeyError:
        response_obj: Dict[str, str] = {
            "status": "failed",
            "message": f"Attribute '{attr}' doesn't exists in request"
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return "", response_obj, http_status

    http_status: int = HTTPStatus.OK

    return attr_name, {"status": "OK", "message": "OK"}, http_status


async def request_json(request: web.Request) -> \
        (Dict[str, Union[str, List[Dict[str, str]]]], Dict[str, str], int):
    """
    Пробуем получить JSON,
    в случае неудачи пишем лог и отправлям ответ.
    """

    try:
        if await request.json() == {}:
            json_data: Dict = {}
        else:
            json_data: Dict[
                str,
                Union[str, List[Dict[str, str]]]
            ] = await request.json()
    except json.decoder.JSONDecodeError:
        response_obj: List[Dict[str, str]] = {
            "status": "failed",
            "message": "JSON doesn't exists in request"
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return [], response_obj, http_status

    http_status: int = HTTPStatus.OK

    return json_data, {"status": "OK", "message": "OK"}, http_status
