from functools import wraps


def multiply(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs) * n
            return result

        return wrapper

    return decorator


@multiply(3)
def add(a, b):
    return a + b


@multiply(10)
def total(*nums):
    return sum(nums)
