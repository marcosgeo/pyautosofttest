def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        found = finder(elem)
        if found.startswith(expected):
            return elem
    return f"Could not find an element with {expected}."

friends = [
    {"name": "Rolf Smith", "age": 32},
    {"name": "John Lennon", "age": 44},
    {"name": "Jessica Jones", "age": 28},
]

def get_friend_by_name(friend):
    return friend["name"]

friend = search(friends, "Jessica", get_friend_by_name)
print(friend)