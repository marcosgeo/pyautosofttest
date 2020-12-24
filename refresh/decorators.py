def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        return f"No admin permission for {user['username']}."
    
    return secure_function

get_admin_password = make_secure(get_admin_password)

user = {"username": "jose", "access_level": "user"}
print(get_admin_password())

user = {"username": "john", "access_level": "admin"}
print(get_admin_password())