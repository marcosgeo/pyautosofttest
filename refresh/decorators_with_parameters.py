import functools

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        return f"No admin permission for {user['username']}."
    
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "other password"

user = {"username": "jose", "access_level": "admin"}
print(get_password("billing"))

user = {"username": "john", "access_level": "admin"}
print(get_password("admin"))