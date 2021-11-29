# 13

## Коммит "Add client_max_size"

1. Актуализировал тест-кейсы, для тестирования POST запроса

2. Добавил client_max_size

3. Оптимизировал функции для заливки данных в БД

# 12

## Коммит "Сorrecting errors 12"

1. Поправил типизацию

2. Добавил комментарии в тест кейсы

# 11

## Коммит "Сorrecting errors 11"

1. Pytest работает

2. Актуализировал `README.txt`

3. Оптимизировал функции в `tests\test_models.py`

# 10

## Коммит "Сorrecting errors 10"

1. Убрал `[0]`, скорректировал в инстукции образец JSON

2. Установил библиотеку `yoyo-migrations`, обновил `requirements.txt`   
    `pip install yoyo-migrations`  
    `pip freeze > requirements.txt`

3. Создал миграции базы данных

4. Скорректировал статусы ответов

5. Перешел на библиотеку `poetry`:
  - `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -` качаю библиотеку
  - `poetry init` создаю файл с конфигурацией
  - `poetry env use python` создаю виртуальное окружение
  - `poetry shell` запускаю виртуальное окружение
  - Добавляю библиотеки:
    - `poetry add asyncpg`
    - `poetry add aiohttp`
    - `poetry add pyyaml`
    - `poetry add ujson`
    - `poetry add loguru`
    - `poetry add -D psycopg2`
    - `poetry add -D pandas`
    - `poetry add -D flake8`
    - `poetry add -D aiohttp_apispec`

8. Удалил `requirements.txt`, `venv`

7. Поменял структуру проекта, актуализировал `README.txt`

8. Создал документацию с помощью библиотеки `aiohttp_apispec`:
   - создал `shemas.py`

9. Создал `routes.py` для удобства настройки API

10. Добавил библиотеку `pytest-aiohttp`:
  - `poetry add -D pytest-aiohttp`

11. Актуализировал типизацию и комментарии

12. Написал тесты, но пока они не работают только для get запроса


# 9

## Коммит "Сorrecting errors 9"

1.  Добавил типизацию в функциях

2. Добавил типизацию переменных

3. Убрал `+` в строках, использовал `.join()`, `.format()`

4. Добавил `HTTPStatus`

5. Уменьшил количество кода при логировании

6. Отработал блоки try/except

7. Создал скрипт, который создает файл `env.yaml`

8. Конфигурация теперь берется из переменных окружения `env.yaml`

9. Актуализировал `README.txt`

10. Разбил функцию реимпорта на несколько функций для каждой таблицы

11. Сделал response красивее

12. Создал функцию для обработки результата SELECT от базы данных

13. Создал скрипт `rewrite_log.py` для очистки `logs.txt`

14. Реализовал подключение к базе данных через pool

15. Добавил логирование через `loguru`, обновил `requirements.txt`

16. Добавил настройки логирования в параметры окружения

17. Создал файл `middlewares.py`, где прописал логику логирования,  
    файл `log_interactions.py` удалил

# 8

## Коммит "Сorrecting errors 8"

1.  Установил библиотеку `flake8`, обновил `requirements.txt`   
    `pip install flake8`  
    `pip freeze > requirements.txt`

2. Исправил ошибки, которые выдавал `flake8`

3. Стандартизировал кавычки:
   - `''` одинарные использую, чтобы указать переменные в массивах
   - `""` двойные для строк, многострочных комментариев, SQL запросов

4. Добавил docstrings

5. Удалил библиотеку `asyncio`, так как она есть в списке стандартных библиотек python

6. Переименовал файл `create_log.py` в `log_interactions.py`

7. Написал приложение в рамках паттерна MVC, актуализировал везде `README.md`

8. Поправил названия переменных и функций

9. Поправил SQL скрипты

10. Убрал префиксы и постфиксы, обозначающие типы данных

11. Убрал не информативные комментарии

12. Скорректировал текст ответа в случае, если для выбранного оператора нет

13. Установил библиотеку `ujson`, обновил `requirements.txt`   
    `pip install ujson`  
    `pip freeze > requirements.txt`

# 7

## Коммит "Add host, port"

1.  В `main.py` прописал возможность выбрать `host`, `port`


# 6

## Коммит "Add logs"

1.  В  `bin` добавил скрипт `create_log.py`, который пишет логи

2.  Логи пишутся в файл `logs.txt`

3. Актуализировал функции в файле `api_interactions.py`, чтобы писались логи


# 5

## Коммит "Beautify project"

1.  В  `README.md` прописал, как запустить проект

2. Создал папку `documentation`, перенес туда `DB_CREATE_SCRIPTS.md`, `DB_SOURCE.md`, `API_INSTRUCTION.md`, создал там файл `README.md`

3. Актуализировал `README.md`

4. Создал папку `bin`, перенес туда исполняемые скрипты `api_interactions.py`, `db_interactions.py`, `calculation.py`, создал там файл `README.md`

5. Создал папку `source`, в ней создал папки `mcc`, файл `README.md`

6. В папке `mcc` создал скрипт `merge_git_ru.py`, он объединяет два исходных файла `mcc_codes_github.csv`, `mcc_codes_ru.csv`, результат возвращает в `mcc_list.txt`

7. Вложил в `mcc` файлы `mcc_codes_github.csv`, `mcc_codes_ru.csv`

8. Создал в `mcc` файл `mcc_list.txt`

9. Установил библиотеку `pandas`: `pip install pandas`

10. Обновляю `requirements.txt`: `pip freeze > requirements.txt`


# 4

## Коммит "Calculation works"

1.  Создал функции:

    -   `mcc_info` для получения информации о МСС по исходным данным

2.  Создал отдельный файл `calculation`, в нем буду описывать вычисления

# 3

## Коммит "Fill data in the data base"

1.  Добавил в README описание файлов `DB_CREATE_SCRIPTS.md`, `DB_SOURCE.md`, `CHANGELOG.md`

2.  Добавил комментарии в код

3.  Создал файл `DB_CREATE_SCRIPTS.md` со скриптами для создания таблиц в БД

4.  Создал файл `DB_SOURCE.md` с описанием того, как получались данные

5.  Создал новые запросы:

    -   `GET` запрос `/table_info`
    -   `POST` запрос `/table_reimport`

6.  Для новых запросов скорректировал функции

7.  Создал файл `API_INSTRUCTION.md`, где описал работу API

8.  Создал таблицы скриптами, описанными в `DB_CREATE_SCRIPTS.md`

9.  С помощью АПИ залил данные в БД

# 2

## Коммит "API works with postgres"

1.  Создал два отдельных файла:  
    `api_interactions.py` описаны функции взаимодействия с АПИ  
    `db_interactions.py` описаны функции взаимодействия с базой данных

2.  Настроил работу с базой данных:  
    `select` при запуске возвращает информацию из таблицы
    `insert` при запуске добавляет в таблицу значения и возвращает все данные из таблицы

# 1

## Коммит "API works"

1.  Прописал в PATH:

-   C:\\Users\\v.kuzmich\\Anaconda3
-   C:\\Users\\v.kuzmich\\Anaconda3\\Scripts
-   C:\\Users\\v.kuzmich\\Anaconda3\\Library\\bin
-   C:\\Program Files\\Git
    ##### ВАЖНО!!! магазин в самый низ перенести!!!
      `C:\Users\v.kuzmich\AppData\Local\Microsoft\WindowsApps`

2.  Устанавливаю aiohttp  
    `pip install aiohttp`

3.  Создаю виртуальное окружение для проекта  
    `python -m venv venv`

4.  Активирую витуальное окружение  
    `venv\Scripts\activate`

5.  Обновляю pip и библиотеки в виртуальном окружении  
    `pip install --upgrade pip`  
    `pip install asyncio`  
    `pip install asyncpg`  
    `pip install aiohttp`  
    `pip freeze > requirements.txt`

6.  Инициализирую новый репозиторий GIT  
    `git init`

7.  Создаю файл `.gitignore`:

-   Создаю файл gitignore.txt
-   Вставляю содержимое с <https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/>
-   Добавляю в конце:  
        #idea
        .idea/
-   В командной строке переименовываю  
    `ren gitignore.txt .gitignore`

8.  Коммит
    `ren gitignore.txt .gitignore`
