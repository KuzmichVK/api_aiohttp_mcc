"""
Тест-кейсы


"""

from http import HTTPStatus

from tests.correct_datas import (
    mcc_codes
)


cases = {
    "table_info": [
        #
        #
        # Проверка правильных запросов GET \table_info
        #
        #
        {
            "parameter": "mcc_codes",
            "response_status": HTTPStatus.OK,
            "json_response": mcc_codes
        },
        #
        #
        # Проверка не правильных запросов GET \table_info
        #
        #
        {
            "parameter": "mcc_code",  # Неверное название таблицы
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "This table isn't in the database"
            }
        },
        {
            "parameter": None,  # Не задан параметр
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Attribute 'table' doesn't exists in request"
            }
        }
    ],
    "post_table": [
        #
        #
        # Проверка не правильных запросов POST \table_reimport
        #
        #
        {
            "parameter": None,  # Не задан параметр
            "json_request": None,  # Не задан JSON
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Attribute 'table' doesn't exists in request"
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": None,  # Не задан JSON
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "JSON doesn't exists in request"
            }
        },
        {
            "parameter": None,  # Не задан параметр
            "json_request": {},  # JSON пустой
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Attribute 'table' doesn't exists in request"
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {},  # JSON пустой
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        {
            "parameter": "mcc_code",  # Неверное название таблицы
            "json_request": {
                "data": [
                    {
                         "mcc": 3043,
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": "text",  # Неверное значение
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": 3043,
                         "edited_description": ";DROP TABLE mcc_codes;",
                         # Пробую удалить таблицу
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status": HTTPStatus.CREATED,
            "json_response": {
                "data": [
                    {
                        "mcc": 3043,
                        "edited_description": ";DROP TABLE mcc_codes;",
                        "combined_description": "AER LINGUS",
                        "russian_name": "Aer Lingus",
                        "russian_description": "null"
                    }
                ]
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": 3043,
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus"
                         # Нету одного параметра
                    }
                ]
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        #
        #
        # Проверка не правильных запросов POST \table_reimport для таблицы
        # mcc_codes
        #
        #
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": "text",  # Не правильный формат
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status":  HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": "text",
                         "edited_description": 10,  # Не правильный формат
                         "combined_description": 20,  # Не правильный формат
                         "russian_name": 30,  # Не правильный формат
                         "russian_description": 40.5  # Не правильный формат
                    }
                ]
            },
            "response_status":  HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect table name or data"
            }
        },
        #
        #
        # Проверка правильных запросов POST \table_reimport для таблицы
        # mcc_codes
        #
        #
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": 3043,
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status":  HTTPStatus.CREATED,
            "json_response": {
                "data": [
                    {
                        "mcc": 3043,
                        "edited_description": "AER LINGUS",
                        "combined_description": "AER LINGUS",
                        "russian_name": "Aer Lingus",
                        "russian_description": "null"
                    }
                ]
            }
        },
        {
            "parameter": "mcc_codes",
            "json_request": {
                "data": [
                    {
                         "mcc": "3043",
                         "edited_description": "AER LINGUS",
                         "combined_description": "AER LINGUS",
                         "russian_name": "Aer Lingus",
                         "russian_description": "null"
                    }
                ]
            },
            "response_status":  HTTPStatus.CREATED,
            "json_response": {
                "data": [
                    {
                        "mcc": 3043,
                        "edited_description": "AER LINGUS",
                        "combined_description": "AER LINGUS",
                        "russian_name": "Aer Lingus",
                        "russian_description": "null"
                    }
                ]
            }
        },
        #
        #
        # Заливка данных в mcc_codes
        #
        #
        {
            "parameter": "mcc_codes",
            "json_request": mcc_codes,
            "response_status": HTTPStatus.CREATED,
            "json_response": mcc_codes
        },
    ],
    "post_calculator": [
        #
        #
        # Проверка не правильных запросов POST \calculator  # noqa: W605
        #
        #
        {
            "parameter": None,
            "json_request": None,  # Нету JSON
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "JSON doesn't exists in request"
            }
        },
        {
            "parameter": None,
            "json_request": {},  # Пустой JSON
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect data in JSON"
            }
        },
        {
            "parameter": None,
            "json_request": {
                "mcc": "txt",  # Не правильный формат
                "num": "300000000"
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect data in JSON"
            }
        },
        {
            "parameter": None,
            "json_request": {
                "mcc": ";DROP TABLE mcc_codes;",  # Попытка удалить таблицу # noqa: E501
                "num_1": "3",
                "num_2": "2",
                "operation": "*"
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect data in JSON"
            }
        },
        {
            "parameter": None,
            "json_request": {
                # Нету одного параметра
                "num_1": "3",
                "num_2": "2",
                "operation": "*"
            },
            "response_status": HTTPStatus.UNPROCESSABLE_ENTITY,
            "json_response": {
                "status": "failed",
                "message": "Incorrect data in JSON"  # noqa: E501
            }
        },
        #
        #
        # Проверка правильных запросов POST \calculator  # noqa: W605
        #
        #
        {
            "parameter": None,
            "json_request": {
                "mcc": "742",
                "num_1": "3",
                "num_2": "2",
                "operation": "*"
            },
            "response_status": HTTPStatus.OK,
            "json_response": {
                "mcc": 742,
                "mcc_name": "Ветеринарные услуги",
                "mcc_description": "Лицензированные специалисты в основном занимающиеся практикой ветеринарии, стоматологии или хирургии для всех видов животных; таких как домашние животные (например, собаки, кошки, рыба), домашний скот и другие фермерские животные (например, рогатый скот, лошади, овцы, свиньи, козы, домашние птицы, пчелы) и экзотические животные.",  # noqa: E501
                "num_1": 3,
                "num_2": 2,
                "operation": "*",
                "result": 6
            }
        },
        {
            "parameter": None,
            "json_request": {
                "mcc": 742,
                "num_1": 3,
                "num_2": 2,
                "operation": "*"
            },
            "response_status": HTTPStatus.OK,
            "json_response": {
                "mcc": 742,
                "mcc_name": "Ветеринарные услуги",
                "mcc_description": "Лицензированные специалисты в основном занимающиеся практикой ветеринарии, стоматологии или хирургии для всех видов животных; таких как домашние животные (например, собаки, кошки, рыба), домашний скот и другие фермерские животные (например, рогатый скот, лошади, овцы, свиньи, козы, домашние птицы, пчелы) и экзотические животные.",  # noqa: E501
                "num_1": 3,
                "num_2": 2,
                "operation": "*",
                "result": 6
            }
        }
    ]
}
