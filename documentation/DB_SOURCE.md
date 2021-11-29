# Способ получения данных:

1.  Таблица МСС `mcc_codes`:

    1.  Скачиваем csv файл с <https://github.com/greggles/mcc-codes/blob/main/mcc_codes.csv>, называем его mcc_codes_github.csv
    2.  Скачиваем csv файл с <https://mcc-codes.ru/code> называем его mcc_codes_ru.csv
    3.  Создаем файл с `json` `mcc_list.txt` с помощью скрипта в `source\mcc\merge_git_ru.py`
    4.  Содержимое файла передаем API:

      -   POST
      -   <http://0.0.0.0:8080/mcc_codes>
      -   в boady передаем содержимое файла mcc_list.txt
