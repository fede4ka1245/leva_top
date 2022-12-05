import peewee
from helpers.tkinter_choose_file import tkinter_choose_file
from helpers.get_new_files import get_new_files
from helpers.get_datatable import get_datatable
from database import database

name = tkinter_choose_file()
files = get_new_files(name)
files.append(name)
datatable = get_datatable(files, name)

Data = peewee.Table("DATA", ('id', 'path'))
Data.bind(database)

for j in range(len(datatable)):
    start_name = files[j][0]

    id = int()

    try:
        id = int(Data.select().order_by(Data.id.desc()).get())
    except:
        id = 100000000

    Data.insert(id=id + 1, path=f'{start_name}:{files[j][2:]}')

    Table = peewee.Table(f'{id + 1}', ('id', 'num', 'mp2', 'emb', 'pin', 'e13'))
    Table.bind(database)

    for i in range(0, len(datatable)):
        Table.insert(
            id={id + 1},
            num=f'{datatable[j][i][0]}',
            mp2=f'{datatable[j][i][1]}',
            pin=f'{datatable[j][i][3]}',
            e13=f'{datatable[j][i][4]}'
        )