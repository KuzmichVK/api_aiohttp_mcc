"""
Файл с миграциями.


"""


import psycopg2 as pg2
from typing import Dict, Union
import yaml

from sql_scripts import script


def sql_execute(conn: pg2.connect, sql: str) -> None:
    """Отправка SQL запроса"""
    try:
        cursor = conn.cursor()
        cursor.execute(
            sql
        )
    except pg2.errors.UndefinedTable:
        pass


with open('env.yaml') as file:
    config: Dict[str, Dict[str, Union[int, str]]] = yaml.safe_load(file)

config_db: Dict[str, str] = config['config_db']

conn = pg2.connect(
    user=config_db['user'],
    password=config_db['password'],
    database=config_db['database'],
    host=config_db['host']
)
conn.autocommit = True

for table in script:
    sql_execute(conn, script[table]['drop'])
    sql_execute(conn, script[table]['create'])

conn.close()
