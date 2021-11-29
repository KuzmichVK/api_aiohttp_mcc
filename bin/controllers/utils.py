"""
В данном модуле описаны функции для работы с базой данных.


"""


from typing import Dict, List


def db_response_to_list_of_dicts(db_response: List) -> List[Dict[str, str]]:
    """Преобразует ответ от базы данных в список словарей"""
    db_response_list: List[Dict[str, str]] = []
    for db_response_i in db_response:
        db_response_dict_i: Dict[str, str] = dict(db_response_i)
        db_response_list.append(db_response_dict_i)
    return db_response_list
