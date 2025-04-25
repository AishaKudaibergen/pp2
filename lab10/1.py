import psycopg2

conn=psycopg2.connect(
    host='localhost', #по умолчанию
    dbname ='pp2',
    user = 'ostgresp',#по умолчанию
    password = 'aishooma*007'
)

# курсор - переходник для взаимодействия
cur =conn.cursor()

cur.execute('select*from students;')
db_ver = cur.fetchall()

print (db_ver)
