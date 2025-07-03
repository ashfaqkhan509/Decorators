"""Write a decorator @timing that measures the time it takes for a function to execute and prints the execution time. 
Apply this decorator to various functions and compare their execution times."""


import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} take {end-start} to execute")

    return wrapper

@timing
def loop():
    for _ in range(500000):
        pass

loop()

@timing
def const_fun(name):
    return f"My name is {name}"

const_fun("Ashfaq Khan")