"""
Скрипты миграций


"""


script = {
    "mcc_codes": {
        "create": """CREATE TABLE mcc_codes (
           mcc                      smallint PRIMARY KEY,
           edited_description       text NOT NULL,
           combined_description     text,
           russian_name             text,
           russian_description      text
           );""",
        "drop": "DROP TABLE mcc_codes;"
    }

    # "table_name": { -- Название таблицы
    #    "create": """CREATE TABLE table_name ( -- Скрипт для создания таблицы
    #       column_1            type_1,
    #       column_2            type_2
    #       );""",
    #    "drop": "DROP TABLE table_name;" -- Скрипт для удаления таблицы
    # },
}
