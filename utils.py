import json
import re
import base64

def load_users(file="data/user_data.json"):
    with open(file, "r") as f:
        return json.load(f)

def save_users(users, file="data/user_data.json"):
    with open(file, "w") as f:
        json.dump(users, f, indent=2)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_strong_password(password):
    return len(password) >= 6 and any(c.isdigit() for c in password)

# def authenticate_user(email, password):
#     users = load_users()
#     for user in users:
#         if user["username"] == email and user["password"] == password:
#             return True
#     return False
def authenticate_user(email, password):
    data = load_users()
    users = data.get("users", [])  # Safely get list of users

    for user in users:
        if isinstance(user, dict):  # Prevent error if malformed
            if user.get("username") == email and user.get("password") == password:
                return True
    return False

def user_exists(email):
    users = load_users()
    return any(user["username"] == email for user in users)

def register_user(first, last, username, password):
    users = load_users()
    users.append({
        "first_name": first,
        "last_name": last,
        "username": username,
        "password": password
    })
    save_users(users)

# import json

def load_places():
    with open("data/places.json", "r") as f:
        return json.load(f)

def get_suggestions(city, preference):
    places_data = load_places()
    city = city.lower()
    preference = preference.lower()
    return places_data.get(city, {}).get(preference, [])



def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
