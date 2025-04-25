import psycopg2
import csv
import re

# Подключение к бд
def connect():
    return psycopg2.connect(
        host='localhost',
        dbname='pp2',
        user='postgres',
        password='aishooma*007'
    )

def setup_database():
    with connect() as conn:
        with conn.cursor() as cur:
            # создать табл если ее не было бы
            cur.execute('''
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    phone VARCHAR(20)
                );
            ''')
            
            # №1 Function to search by pattern
            cur.execute('''
                CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
                RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY 
                    SELECT phonebook.id, phonebook.name, phonebook.phone 
                    FROM phonebook 
                    WHERE phonebook.name ILIKE '%' || pattern || '%' 
                    OR phonebook.phone ILIKE '%' || pattern || '%';
                END;
                $$ LANGUAGE plpgsql;
            ''')
            
            #№2 Procedure to insert or update user
            cur.execute('''
                CREATE OR REPLACE PROCEDURE insert_or_update_user(
                    p_name VARCHAR, 
                    p_phone VARCHAR
                )
                AS $$
                BEGIN
                    -- Check if user exists
                    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
                        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
                    ELSE
                        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
                    END IF;
                END;
                $$ LANGUAGE plpgsql;
            ''')
            
            # №3 Procedure to insert many users with validation
            cur.execute('''
                CREATE OR REPLACE PROCEDURE insert_many_users(
                    INOUT invalid_data REFCURSOR,
                    users_name VARCHAR[],
                    users_phone VARCHAR[]
                )
                AS $$
                DECLARE
                    i INTEGER;
                    phone_regex TEXT := '^\+?[0-9]{10,15}$'; -- Basic phone number validation
                BEGIN
                    -- Open cursor for invalid data
                    OPEN invalid_data FOR 
                        SELECT 'Invalid data' AS error, '' AS name, '' AS phone 
                        WHERE 1=0; -- Empty result set with correct structure
                    
                    -- Check arrays have same length
                    IF array_length(users_name, 1) <> array_length(users_phone, 1) THEN
                        RAISE EXCEPTION 'Arrays must have the same length';
                    END IF;
                    
                    -- Process each user
                    FOR i IN 1..array_length(users_name, 1) LOOP
                        -- Validate phone number
                        IF users_phone[i] ~ phone_regex THEN
                            -- Valid phone - insert or update
                            CALL insert_or_update_user(users_name[i], users_phone[i]);
                        ELSE
                            -- Invalid phone - add to result
                            INSERT INTO invalid_data (error, name, phone) 
                            VALUES ('Invalid phone', users_name[i], users_phone[i]);
                        END IF;
                    END LOOP;
                END;
                $$ LANGUAGE plpgsql;
            ''')
            
            #№4 Function for pagination
            cur.execute('''
                CREATE OR REPLACE FUNCTION get_records_with_pagination(
                    lim INTEGER,
                    offs INTEGER
                )
                RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY 
                    SELECT phonebook.id, phonebook.name, phonebook.phone 
                    FROM phonebook 
                    ORDER BY name
                    LIMIT lim OFFSET offs;
                END;
                $$ LANGUAGE plpgsql;
            ''')
            
            # №5 Procedure to delete by username or phone
            cur.execute('''
                CREATE OR REPLACE PROCEDURE delete_user(
                    p_name VARCHAR DEFAULT NULL,
                    p_phone VARCHAR DEFAULT NULL
                )
                AS $$
                BEGIN
                    IF p_name IS NOT NULL AND p_phone IS NOT NULL THEN
                        DELETE FROM phonebook WHERE name = p_name OR phone = p_phone;
                    ELSIF p_name IS NOT NULL THEN
                        DELETE FROM phonebook WHERE name = p_name;
                    ELSIF p_phone IS NOT NULL THEN
                        DELETE FROM phonebook WHERE phone = p_phone;
                    ELSE
                        RAISE NOTICE 'No deletion criteria provided';
                    END IF;
                END;
                $$ LANGUAGE plpgsql;
            ''')
    print("Database setup complete.")

# Функция для поиска по шаблону
def search_by_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.callproc('search_by_pattern', (pattern,))
            results = cur.fetchall()
            for row in results:
                print(row)

# Процедура для вставки или обновления пользователя
def insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            # Используем CALL
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            conn.commit()  # Важно для процедур
    print("Operation completed.")

# Процедура для вставки нескольких пользователей
def insert_many_users(names, phones):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                names_list = [n.strip() for n in names.split(',')]
                phones_list = [p.strip() for p in phones.split(',')]
                
                if len(names_list) != len(phones_list):
                    print("Error: Names and phones count mismatch")
                    return
                
                # Создаем временную таблицу для результатов
                cur.execute("""
                    CREATE TEMP TABLE IF NOT EXISTS temp_invalid_data (
                        error TEXT,
                        name VARCHAR,
                        phone VARCHAR
                    ) ON COMMIT DROP;
                    TRUNCATE temp_invalid_data;
                """)
                
                # Вызываем процедуру
                cur.execute("""
                    CALL insert_many_users('invalid_data', %s::VARCHAR[], %s::VARCHAR[]);
                    FETCH ALL FROM invalid_data;
                """, (names_list, phones_list))
                
                # Получаем результаты
                invalid_data = cur.fetchall()
                if invalid_data:
                    print("\nInvalid data found:")
                    for row in invalid_data:
                        print(row)
                else:
                    print("All data processed successfully!")
                
                conn.commit()
                
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

# Функция для пагинации
def get_records_with_pagination(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.callproc('get_records_with_pagination', (limit, offset))
            results = cur.fetchall()
            for row in results:
                print(row)

# Процедура для удаления пользователя
def delete_user(name=None, phone=None):
    if name is None and phone is None:
        print("Please provide either name or phone.")
        return
    
    with connect() as conn:
        with conn.cursor() as cur:
            # Используем CALL для процедуры 
            if name and phone:
                cur.execute("CALL delete_user(%s, %s)", (name, phone))
            elif name:
                cur.execute("CALL delete_user(%s, NULL)", (name,))
            elif phone:
                cur.execute("CALL delete_user(NULL, %s)", (phone,))
            conn.commit() 
    print("Deletion completed.")

# Главное меню
def menu():
    setup_database()
    while True:
        print("\n📱 ENHANCED PHONEBOOK MENU")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Insert many users")
        print("4. View with pagination")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == '1':
            pattern = input("Enter search pattern: ")
            search_by_pattern(pattern)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif choice == '3':
            names = input("Enter names separated by comma: ").split(',')
            phones = input("Enter phones separated by comma: ").split(',')
            insert_many_users(names, phones)
        elif choice == '4':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            get_records_with_pagination(limit, offset)
        elif choice == '5':
            print("Delete by:")
            print("1. Name")
            print("2. Phone")
            print("3. Both")
            delete_choice = input("Choose (1-3): ")
            if delete_choice == '1':
                delete_user(name=input("Enter name: "))
            elif delete_choice == '2':
                delete_user(phone=input("Enter phone: "))
            elif delete_choice == '3':
                delete_user(name=input("Enter name: "), phone=input("Enter phone: "))
            else:
                print("Invalid choice")
        elif choice == '6':
            print("Goodbye!")
            break

if __name__ == "__main__":
    menu()