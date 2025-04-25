import psycopg2
import csv

# подключение к бд
def connect():
    return psycopg2.connect(
    host='localhost', #по умолчанию
    dbname ='pp2',
    user = 'postgres',#по умолчанию
    password = 'aishooma*007'
)

#создание табл
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    phone VARCHAR(20)
                );
            ''')
    print("Table ensured.")

# Вставка данных с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Added!")

# Вставка данных из CSV
def insert_from_csv(path):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                with open(path, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) != 2:
                            print(f" Skipping invalid row: {row}")
                            continue
                        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        print("CSV imported!")
    except Exception as e:
        print("Error importing CSV:", e)

# Обновление номера по имени
def update_user(name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    print("Updated!")

# Показать всех
def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# Поиск по имени
def query_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
            print(cur.fetchall())

# Поиск по номеру
def query_by_phone(phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
            print(cur.fetchall())

# Удаление по имени
def delete_user(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    print("Deleted!")

# Главная
def menu():
    create_table()
    while True:
        print("\n📱 PHONEBOOK MENU")
        print("1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update user")
        print("4. View all")
        print("5. Search by name")
        print("6. Search by phone")
        print("7. Delete user")
        print("8. Exit")

        choice = input("Choose (1-8): ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Enter CSV path: "))
        elif choice == '3':
            update_user(input("Name to update: "), input("New phone: "))
        elif choice == '4':
            query_all()
        elif choice == '5':
            query_by_name(input("Name: "))
        elif choice == '6':
            query_by_phone(input("Phone: "))
        elif choice == '7':
            delete_user(input("Name to delete: "))
        elif choice == '8':
            print(" Goodbye!")
            break

if __name__ == "__main__":
    menu()
