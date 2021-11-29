"""
Описание схем


"""

from typing import Dict, List
from marshmallow import Schema, fields


class Table_row(Schema):
    """Описание строки таблицы"""
    column_1: str = fields.String(required=True)
    column_2: str = fields.String(required=True)
    column_3: str = fields.String(required=True)


class Calc_request(Schema):
    """Описание запроса к калькулятору"""
    mcc: str = fields.String(required=True)
    num_1: str = fields.String(required=True)
    num_2: str = fields.String(required=True)
    operation: str = fields.String(required=True)


class Calc_response(Calc_request):
    """Описание ответа от калькулятора"""
    mcc_name: str = fields.String(required=True)
    mcc_description: str = fields.String(required=True)
    result: str = fields.String(required=True)


class Table_data(Schema):
    """Описание таблицы"""
    data: List[Dict[str, str]] = fields.List(fields.Nested(Table_row))


class Table_name(Schema):
    """Описание названия таблицы"""
    table: str = fields.String(required=True)
