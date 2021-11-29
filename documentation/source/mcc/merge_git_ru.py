# импорт библиотек
import pandas as pd
import json

# чтение файлов
mcc_git = pd.read_csv(r'documentation\source\mcc\mcc_codes_github.csv')
mcc_ru = pd.read_csv(r'documentation\source\mcc\mcc_codes_ru.csv')

# объединение файлов
mcc_all = mcc_git.merge(mcc_ru, on='mcc', how='left')

# отбор и переименование нужных столбцов
mcc_all = mcc_all[[
    'mcc',
    'edited_description',
    'combined_description',
    'name',
    'description'
]]
mcc_all = mcc_all.rename(
    columns={
        'name': 'russian_name',
        'description': 'russian_description'
    }
)

# заполняем пропуски
mcc_all = mcc_all.fillna('null')

# преобразовываю в строки
mcc_all['mcc'] = mcc_all['mcc'].astype('str')

# преобразование в список
mcc_list = mcc_all.to_dict('records')

# преобразование в JSON
mcc_json = json.dumps({"data": mcc_list}, ensure_ascii=False)

# запись в файл
with open(
        r'documentation\source\mcc\mcc_list.txt',
        'w',
        encoding="utf-8"
        ) as file:
    file.write(mcc_json)
