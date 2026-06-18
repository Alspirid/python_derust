def safe_int(s: str, default=0) -> int:
    try:
        return int(s)
    except ValueError:
        return default


class InsufficientFunds(Exception):
    pass


def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise InsufficientFunds(f"Insufficient balance: {amount} > {balance}")
    return balance - amount


# try:
#     withdraw(100, 150)
# except InsufficientFunds as e:
#     print(e)  # → Insufficient balance: 150 > 100


class InvalidPrice(ValueError):
    pass


def parse_price(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise InvalidPrice(f"Invalid price: {s}") from e


# try:
#     parse_price("abc")
# except InvalidPrice as e:
#     print(e)  # → Invalid price: abc


def process(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("error")
        return -1
    else:
        print("ok")
        return result
    finally:
        print("done")


print(process(2))  # prints? returns?
# print(process(0))   # prints? returns?
