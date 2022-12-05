from configparser import ConfigParser
import psycopg2
import os.path

config = ConfigParser()
config.read('settings.ini')
dbfacts = config['database']
folder = config['path']
files = []
path = folder['path'].replace('"', '')

con = psycopg2.connect(
    dbname=dbfacts['dbname'],
    user=dbfacts['user'],
    password=dbfacts['password'],
    host=dbfacts['host']
)

cur = con.cursor()

def get_new_files(name):
    try:
        cur.execute('''SELECT path FROM data ORDER BY path''')
        query = [i[0] for i in cur.fetchall()]
        print(path)
        print(query)
        if folder['path'] and os.path.exists(path):
            for i in os.listdir(path):
                if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                          -4:] == 'xlsx') and f'{path}/{i}' not in query and f'{path}/{i}' != name:
                    files.append(f'{path}/{i}')
        print(files)
    except:
        if folder['path'] and os.path.exists(path):
            for i in os.listdir(path):
                if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                          -4:] == 'xlsx') and f'{path}/{i}' != name:
                    files.append(f'{path}/{i}')
    finally:
        return files
