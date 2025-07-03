"""Create a decorator @repeat(n) that repeats the decorated function n times.
It should also accept an argument for whether to print the results each time.
Apply this decorator to a simple function."""


def repeat(n, print_result=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                if print_result:
                    print(result)

            print(f"Function call {n} times")

        return wrapper

    return decorator


@repeat(5)
def simple_fun():
    return "Ashfaq khan"


simple_fun()
