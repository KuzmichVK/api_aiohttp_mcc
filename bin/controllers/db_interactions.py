"""
В данном модуле описаны функции для работы с базой данных.


"""


import yaml
import decimal
import asyncpg
from typing import Dict, List, Union, Any

from bin.controllers.utils import db_response_to_list_of_dicts


with open('env.yaml') as file:
    config: Dict[str, Dict[str, Union[int, str, List[str]]]] = \
        yaml.safe_load(file)


async def mcc_info(request_data: Dict[str, Any], pool) -> \
        List[Dict[str, str]]:
    """Функция, которая возвращает данные о МСС"""

    async with pool.acquire() as conn:
        values_selected: List = await conn.fetch(
            """
            SELECT
                -- Если есть русское название/описание, то берем их
                CASE
                    WHEN russian_name is not null THEN russian_name
                    ELSE edited_description
                END as mcc_name,
                CASE
                    WHEN russian_description is not null
                    THEN russian_description
                    ELSE combined_description
                END as mcc_description
            FROM
                mcc_codes
            WHERE
                mcc = $1
            """, request_data['mcc']
        )

    return db_response_to_list_of_dicts(values_selected)[0]


async def select_sql(table_name: str, pool) -> (str, List[Dict[str, str]]):
    """Функция, которая возвращает данные из таблицы"""

    if table_name in config['config_db_tables']:
        async with pool.acquire() as conn:
            values_selected: List = await conn.fetch(
                f"""SELECT * FROM {table_name}"""
                )
        db_status: str = "OK"
    else:
        db_status: str = f"UndefinedTableError: '{table_name}'"
        values_selected: List = []

    return db_status, db_response_to_list_of_dicts(values_selected)


async def reimport_table(request_data: List[Dict[str, Any]], table_name: str, pool) \
        -> (str, List[Dict[str, str]]):
    """
    Функция, которая выбирает функцию для реимпорта таблицы, отлавливает
    ошибки, возвращает данные из таблицы.
    """

    try:
        async with pool.acquire() as conn:
            async with conn.transaction():
                if table_name == "mcc_codes":
                    db_status = await reimport_mcc_codes(
                        request_data,
                        conn
                    )
                    """
                    В целях безопасности для каждой таблицы создается своя
                    функция реимпорта. Необходимо:
                    1. Создать функцию аналогичную
                       reimport_mcc_codes
                    2. Дописать еще один блок elif
                    3. Занести название таблицы в переменную окружения
                       config_db_tables
                    """
                else:
                    db_status: str = "ERROR: Incorrect table name"

        values_selected: List = []

        if db_status == "OK":
            return await select_sql(table_name, pool)
        else:
            return db_status, values_selected
    except ValueError as exc:
        db_status: str = f"ValueError: {str(exc)}"
    except decimal.InvalidOperation as exc:
        db_status: str = f"decimal.InvalidOperation: {str(exc)}"
    except IndexError as exc:
        db_status: str = f"IndexError: {str(exc)}"
    except asyncpg.exceptions.UniqueViolationError as exc:
        db_status: str = f"asyncpg.exceptions.UniqueViolationError: {str(exc)}"

    values_selected: List = []

    return db_status, values_selected


async def reimport_mcc_codes(request_data: List[Dict[str, Any]], conn) \
        -> str:
    """
    Функция, которая очищает таблицу mcc_codes, вставляет данные в
    нее.
    """

    await conn.execute("""TRUNCATE mcc_codes;""")
    request_data_list: list = []
    for request_data_i in request_data:
        values_list: List[Any] = []
        for request_data_i_i in request_data_i:
            values_list.append(request_data_i[
                str(request_data_i_i)
            ])
        values_list[0] = int(values_list[0])
        for i in range(1, 4):
            values_list[i] = str(values_list[i])

        request_data_list.append(tuple(values_list))

    await conn.copy_records_to_table(
        'mcc_codes',
        records=request_data_list
    )
    return "OK"
