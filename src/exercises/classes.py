from __future__ import annotations


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_to(self, p: Point) -> float:
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Point class: x={self.x}, y={self.y}"

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y
