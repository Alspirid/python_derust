from typing import Protocol


class HasArea(Protocol):
    def area(self) -> float:
        return self.area()


class Circle:
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float: ...


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side**2


def total_area(items: list[HasArea]) -> float:
    return sum(x.area() for x in items)


# print(total_area([Circle(1), Square(2)]))  # → ~7.14
