from helpers.tkinter_choose_file import tkinter_choose_file
from helpers.get_new_files import get_new_files
from helpers.get_datatable import get_datatable
from database.orm.Data import Data
from database.orm.IndexedTable import IndexedTable

name = tkinter_choose_file()

files = get_new_files(name)
files.append(name)

datatable = get_datatable(files, name)

Data.create_table()

for j in range(len(datatable)):
    start_name = files[j][0]

    id = int()

    try:
        id = int(str(Data.select().order_by(Data.id.desc()).get()))
    except:
        id = 100000000

    Data.insert(id=id + 1, path=f'{start_name}:{files[j][2:]}').execute()

    indexedTable = IndexedTable()
    indexedTable._meta.table_name = str(id + 1)

    indexedTable.create_table()

    for i in range(0, len(datatable[j])):
        indexedTable.insert(
            index=f'{i}',
            num=f'{datatable[j][i][0]}',
            mp2=f'{datatable[j][i][1]}',
            emb=f'{datatable[j][i][2]}',
            pin=f'{datatable[j][i][3]}',
            e13=f'{datatable[j][i][4]}'
        ).execute()