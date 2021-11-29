"""
В данном модуле описана функция, которая пишет логи в файл.


"""


import yaml
from aiohttp import web
from loguru import logger
from http import HTTPStatus
from typing import Dict, Union

from bin.views.api_interactions import request_json


with open("env.yaml") as file:
    config: Dict[str, Dict[str, Union[int, str]]] = yaml.safe_load(file)

logger_config: Dict[str, str] = config['config_log']

logger.add(
    logger_config['path'],
    format=logger_config['format'],
    level=logger_config['level'],
    rotation=logger_config['rotation'],
    compression=logger_config['compression'],
    encoding=logger_config['encoding']
)


@web.middleware
async def middleware_to_log(request, handler):
    """Промежуточная функция для логирования"""
    logger.info(request)
    logger.info(f"URL: {str(request.url)}")
    request_json_data, request_json_info, request_http_status = \
        await request_json(request)
    if request_json_info['status'] == "OK":
        logger.info(f"Request JSON INFO: {str(request_json_data)}")
    else:
        logger \
            .info(f"Request JSON INFO: {str(request_json_info['message'])}")

    response = await handler(request)

    try:
        if (response.status == HTTPStatus.OK) or \
                (response.status == HTTPStatus.CREATED):
            logger.info(f"Response JSON INFO: {response.text}")
        else:
            logger.warning(f"Response JSON INFO: {response.text}")
    except AttributeError as exc:
        logger.info(f"Response doesn't exist JSON: {exc}")
    return response
