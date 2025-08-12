# Decorator practice

import time
import functools

def timer_decorator(func):
    """Decorator that prints how long a function takes to run."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.2f} seconds to complete.")
        return result
    return wrapper_timer

def log_decorator(func):
    """Decorator that logs function name, arguments, and return value."""
    @functools.wraps(func)
    def wrapper_log(*args, **kwargs):
        print(f"Calling function: '{func.__name__}'")
        print(f"  Arguments: {args}")
        print(f"  Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper_log

@log_decorator
@timer_decorator
def add_numbers(x, y):
    """Adds two numbers with a simulated delay."""
    time.sleep(2)
    return x + y

def main():
    add_numbers(3, 5)
    add_numbers(3, 150)

if __name__ == "__main__":
    main()