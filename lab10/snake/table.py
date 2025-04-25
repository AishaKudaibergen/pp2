import psycopg2

config = {
    'dbname': 'pp2',
    'user': 'postgres', 
    'password': 'aishooma*007'
}

def get_connection():
    return psycopg2.connect(**config)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            username TEXT PRIMARY KEY,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_scores WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def add_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_scores (username) VALUES (%s)", (username,))
    conn.commit()
    cursor.close()
    conn.close()

def update_score_and_level(username, new_score, new_level):
    conn = get_connection()
    cursor = conn.cursor()
    
    # getting the current data
    cursor.execute("SELECT score, level FROM user_scores WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        current_score, current_level = result
        # if the user has broken the record
        if new_score > current_score:
            cursor.execute("""
                UPDATE user_scores
                SET score = %s, level = %s
                WHERE username = %s
            """, (new_score, new_level, username))
    
    conn.commit()
    cursor.close()
    conn.close()