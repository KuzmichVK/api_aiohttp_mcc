# Скрипты для создания таблиц в БД:

1. Таблица с МСС:
```sql
CREATE TABLE mcc_codes (
    mcc                      smallint PRIMARY KEY,
    edited_description       text NOT NULL,
    combined_description     text,
    russian_name             text,
    russian_description      text
);
```
