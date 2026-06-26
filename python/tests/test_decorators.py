from exercises.decorators import add, total


def test_add():
    assert add(2, 3) == 15


def test_total():
    assert total(1, 2, 3) == 60
