"""Create a decorator called @uppercase_decorator
that converts the result of a function to uppercase.
Apply this decorator to a function that
returns a string and test it."""


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))

        return result.upper()

    return wrapper


@uppercase_decorator
def welcome():
    return "Welcome Ashfaq"


print(welcome())
