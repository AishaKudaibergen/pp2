from table import init_db, get_user, add_user

def user_login():
    init_db()
    username = input("Enter your username: ").strip()

    user = get_user(username)
    if user:
        print(f"Welcome back, {username}! Your record: {user[1]} points, level {user[2]}")
    else:
        print(f"A new user has been created: {username}")
        add_user(username)
    return username, 0, 1