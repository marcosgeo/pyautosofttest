import functools

def decorator_factory(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            return f"No {access_level} permissions for {user['username']}."
        
        return secure_function
    return decorator

@decorator_factory("admin")
def get_admin_password():
    return "admin: 1234"

@decorator_factory("user")
def get_dashboard_password():
    return "user: user_password"

#user = {"username": "jose", "access_level": "user"}
user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())

print(get_admin_password())
print(get_dashboard_password())