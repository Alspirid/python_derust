from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def distance_to(self, p: Point) -> float:
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
