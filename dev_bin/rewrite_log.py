"""
Данный модуль очищает файл logs.txt.


"""


import yaml
from typing import Dict, Union

with open('env.yaml') as file:
    config: Dict[str, Dict[str, Union[int, str]]] = yaml.safe_load(file)

with open(config['config_log']['path'], "w", encoding="utf-8") as file:
    file.write("")
