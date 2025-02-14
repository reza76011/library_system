def add_user(name, family, father_name, code, birthday):
    users = load_data("users.dat")
    user_id = len(users)
    users[user_id] = [name, family, father_name, code, birthday]
    save_data("users.dat", users)
    print(f"User added. User ID: {user_id}")