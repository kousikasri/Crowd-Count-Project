users = [
    {
        "username": "admin",
        "role": "admin",
        "status": "Active",
        "last_login": "2026-01-04 20:30:00"
    },
    {
        "username": "operator1",
        "role": "user",
        "status": "Active",
        "last_login": "2026-01-04 18:10:22"
    },
    {
        "username": "operator2",
        "role": "user",
        "status": "Inactive",
        "last_login": None
    }
]

def get_users():
    return users

def toggle_user(username):
    for u in users:
        if u["username"] == username:
            u["status"] = "Inactive" if u["status"] == "Active" else "Active"
            return u

def change_role(username, new_role):
    for u in users:
        if u["username"] == username:
            u["role"] = new_role
            return u

def delete_user(username):
    global users
    users = [u for u in users if u["username"] != username or u["role"] == "admin"]
