import pytest

from exercises.dataclass import Point


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Point(0, 0), Point(3, 4), 5.0),
        (Point(0, 0), Point(0, 0), 0.0),
        (Point(1, 1), Point(2, 2), 2**0.5),
    ],
)
def test_distance_to(a, b, expected):
    assert a.distance_to(b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Point(1, 2), Point(1, 2), True),
        (Point(1, 2), Point(9, 2), False),
        (Point(1, 2), Point(1, 9), False),
        (Point(1, 2), 123, False),
    ],
)
def test_point_equality(a, b, expected):
    assert (a == b) is expected


def test_repr():
    assert repr(Point(1, 2)) == "Point(x=1, y=2)"
