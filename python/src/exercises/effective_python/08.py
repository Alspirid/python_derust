# Walrus operator
#
fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}


def make_lemonade(c: int): ...


def out_of_stock(): ...


if count := fresh_fruit.get("lemon", 0):
    make_lemonade(count)
else:
    out_of_stock()
