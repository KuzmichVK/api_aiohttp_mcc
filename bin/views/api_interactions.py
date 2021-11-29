"""
В данном модуле описаны функции для обработки API запросов.


"""


import ujson
from aiohttp import web
from http import HTTPStatus
from decimal import Decimal
from typing import Dict, Any, List
from aiohttp_apispec import (
    docs,
    request_schema,
    querystring_schema
)

from bin.models.calculation import (
    calculator
)
from bin.views.utils import request_table_name, request_json
from bin.controllers.db_interactions import (
    select_sql,
    reimport_table,
    mcc_info
)
from bin.views.schemas import (
    Table_data,
    Calc_request,
    Calc_response,
    Table_name
)


@docs(
    tags=["Table interactions"],
    summary="Get table data",
    description="""Get data from tables:
        mcc_codes""",
    responses={
        HTTPStatus.OK: {
            "description": "Ok. Table Data",
            "schema": Table_data
        },
        HTTPStatus.UNPROCESSABLE_ENTITY: {
            "description": """This table isn't in the database;
                Attribute 'table' doesn't exists in request"""
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "description": "Server error"
        }
    }
)
@querystring_schema(Table_name)
async def get_table(request: web.Request) -> web.Response:
    """Выполняется GET запрос /table_info"""

    table_name, response_obj, http_status = \
        await request_table_name(request, "table")
    """Проверяем, нет ли ошибки в атрибуте 'table' запроса"""
    if response_obj['status'] != "OK":
        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    db_status, response_obj = await select_sql(
        table_name,
        request.app['pool']
    )
    """Проверяем, нет ли ошибки работе БД"""
    if db_status != "OK":
        response_obj: Dict[str, str] = {
            "status": "failed",
            "message": "This table isn't in the database"
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    http_status: int = HTTPStatus.OK

    return web.Response(
            text=ujson.dumps(
                {"data": response_obj},
                ensure_ascii=False
            ),
            status=http_status,
            content_type="application/json"
        )


@docs(
    tags=["Table interactions"],
    summary="Post table data",
    description="""Post data to tables:
        mcc_codes
        """,
    responses={
        HTTPStatus.CREATED: {
            "description": "Ok. Table created",
            "schema": Table_data
        },
        HTTPStatus.UNPROCESSABLE_ENTITY: {
            "description": """This table isn't in the database;
                Attribute 'table' doesn't exists in request;
                JSON doesn't exists in request;
                Incorrect table name or data"""
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "description": "Server error"
        }
    }
)
@querystring_schema(Table_name)
@request_schema(Table_data)
async def post_table(request: web.Request) -> web.Response:
    """Выполняется POST запрос /table_reimport"""

    table_name, response_obj, http_status = \
        await request_table_name(request, "table")
    """Проверяем, нет ли ошибки в атрибуте 'table' запроса"""
    if response_obj['status'] != "OK":
        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    table_data, response_obj, http_status = await request_json(request)
    """Проверяем, есть ли JSON в запросе"""
    if response_obj['status'] != "OK":
        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    """Вызов функции, которая вставляет данные, получение ответа от нее"""
    try:
        db_status, response_obj = await reimport_table(
            table_data['data'],
            table_name,
            request.app['pool']
        )
    except KeyError:
        response_obj: Dict[str, str] = {
            "status": "failed",
            "message": "Incorrect table name or data"
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    """Проверяем, нет ли ошибки работе БД"""
    if db_status != "OK":
        response_obj: Dict[str, str] = {
            "status": "failed",
            "message": "Incorrect table name or data"
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    http_status: int = HTTPStatus.CREATED

    return web.Response(
            text=ujson.dumps(
                {"data": response_obj},
                ensure_ascii=False
            ),
            status=http_status,
            content_type="application/json"
        )


@docs(
    tags=["Calculator"],
    summary="Calculate",
    description="""Calculate:
        num_1 operation num_2 =
        """,
    responses={
        HTTPStatus.OK: {
            "description": "Ok. Calculated",
            "schema": Calc_response
        },
        HTTPStatus.UNPROCESSABLE_ENTITY: {
            "description": """JSON doesn't exists in request;
                Incorrect data in JSON;
                """
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "description": "Server error"
        }
    }
)
@request_schema(Calc_request)
async def post_calculator(request: web.Request) -> web.Response:
    """Выполняется POST запрос /calculator"""

    calc_data, response_obj, http_status = await request_json(request)

    """Проверяем, есть ли JSON в запросе"""
    if response_obj['status'] != "OK":
        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    """Проверяем, соответствие JSON нужному формату"""
    try:
        calc_data['mcc']: int = int(calc_data['mcc'])
        calc_data['num_1']: Decimal() = Decimal(calc_data['num_1'])
        calc_data['num_2']: Decimal() = Decimal(calc_data['num_2'])
        calc_data['operation']: str = str(calc_data['operation'])
    except (ValueError, KeyError):
        response_message: str = """Incorrect data in JSON"""
        response_obj: Dict[str, str] = {
            "status": "failed",
            "message": response_message
        }

        http_status: int = HTTPStatus.UNPROCESSABLE_ENTITY

        return web.Response(
                text=ujson.dumps(
                    response_obj,
                    ensure_ascii=False
                ),
                status=http_status,
                content_type="application/json"
            )

    """Получение данных о МСС"""
    try:
        mcc_info_list: Dict[str, str] = \
            await mcc_info(calc_data, request.app['pool'])
    except IndexError:
        mcc_info_list: Dict[str, str] = {
            "mcc_name": "Нету данного МСС в БД",
            "mcc_description": "Нету данного МСС в БД"
        }

    """
    Вызов функций, которые считают результат
    """
    result: Decimal() = await calculator(calc_data)

    response_obj: List[Dict[str, Any]] = {
        "mcc": calc_data['mcc'],
        "mcc_name": mcc_info_list['mcc_name'],
        "mcc_description": mcc_info_list['mcc_description'],
        "num_1": calc_data['num_1'],
        "num_2": calc_data['num_2'],
        "operation": calc_data['operation'],
        "result": result
    }

    http_status: int = HTTPStatus.OK

    return web.Response(
            text=ujson.dumps(
                response_obj,
                ensure_ascii=False
            ),
            status=http_status,
            content_type="application/json"
        )
