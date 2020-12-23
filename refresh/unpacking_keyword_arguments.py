def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


details = {"name": "john", "age": 29}
print_nicely(**details)

print_nicely(key="bob", value="55")


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 2, 8, name="john", age=44)
