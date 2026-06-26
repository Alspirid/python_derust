from functools import cache


@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(30))
print(fib.cache_info())
print(fib.cache_parameters())
