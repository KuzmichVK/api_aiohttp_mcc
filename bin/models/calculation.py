"""
В данном модуле описаны функции для вычисления корректной ставки.


"""


import yaml
from typing import Dict, List, Any, Union

with open('env.yaml') as file:
    config: Dict[str, Dict[str, Union[int, str, List[str]]]] = \
        yaml.safe_load(file)


async def calculator(request_data: Dict[str, Any]) -> Any:
    """Функция считает результат"""

    if request_data['operation'] == '*':
        return request_data['num_1'] * request_data['num_2']
    elif request_data['operation'] == '+':
        return request_data['num_1'] + request_data['num_2']
    elif request_data['operation'] == '-':
        return request_data['num_1'] - request_data['num_2']
    elif request_data['operation'] == '/':
        return request_data['num_1'] / request_data['num_2']
    else:
        return 'Неизвестная операция'
