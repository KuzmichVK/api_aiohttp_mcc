"""
Данный модуль создает файл env.yaml


"""


import yaml
from typing import Dict, Union, List

"""Задаются конфигурации для приложения"""
config_app: Dict[str, Union[int, str]] = {
    "port": 8080,
    "host": "0.0.0.0",
    "client_max_size": 10*1024**2
}

"""Задаются конфигурации для базы данных"""
config_db: Dict[str, str] = {
    "user": "test_user",
    "password": "12345",
    "database": "test",
    "host": "localhost"
}

"""Задаются конфигурации для логов"""
config_log: Dict[str, str] = {
    "path": "logs/log.log",
    "format": "{time} {level} {message}",
    "level": "INFO",
    "rotation": "10 MB",
    "compression": "zip",
    "encoding": "utf8"
}

"""Задаются названия таблиц в БД"""
config_db_tables: List[str] = [
    "mcc_codes"
]

config: Dict[str, Dict[str, str]] = {
    "config_app": config_app,
    "config_db": config_db,
    "config_log": config_log,
    "config_db_tables": config_db_tables
}

file = open('env.yaml', 'w')
file.write(yaml.dump(config))
file.close
