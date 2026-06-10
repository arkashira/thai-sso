import hashlib

def login(username, password):
    user = get_user(username)
    if user and hashlib.sha256(password.encode()).hexdigest() == user.password:
        session = create_session(user)
        return session
    else:
        return None