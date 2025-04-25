import psycopg2

conn=psycopg2.connect(
    host='localhost', #по умолчанию
    dbname ='pp2',
    user = 'postgres',#по умолчанию
    password = 'aishooma*007'
)

# курсор - переходник для взаимодействия
cur =conn.cursor()

cur.execute("""
Create table orders(
    id serial primary key,
    name varchar(100),
    price numeric 
            )
            """)
conn.commit ()

print('table created successfully')

#closing

cur.close()
conn.close()