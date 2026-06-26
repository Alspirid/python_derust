import pytest

from exercises.warm_up.generators_and_args import (
    add_tag,
    average,
    common,
    make_user,
    running_total,
)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([], []),
    ],
)
def test_running_total(nums, expected):
    # running_total is a generator, so materialise it with list() before comparing.
    assert list(running_total(nums)) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ((1, 2, 3, 4), 2.5),
        ((10,), 10.0),
        ((), 0.0),
    ],
)
def test_average(nums, expected):
    # pytest.approx guards against float rounding (good habit even when exact here).
    assert average(*nums) == pytest.approx(expected)


@pytest.mark.parametrize(
    "params, expected",
    [
        ({"name": "alice", "age": 30}, {"name": "alice", "age": 30, "role": "user"}),
        ({"name": "bob", "role": "admin"}, {"name": "bob", "role": "admin"}),
    ],
)
def test_make_user(params, expected):
    assert make_user(**params) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4], [3, 4, 5, 6], {3, 4}),
        ([1, 2], [3, 4], set()),
    ],
)
def test_common(a, b, expected):
    assert common(a, b) == expected


def test_add_tag_appends_to_given_list():
    assert add_tag("python", ["go"]) == ["go", "python"]


def test_add_tag_does_not_share_state_between_calls():
    # The None-sentinel default avoids the classic mutable-default-argument trap:
    # each call with no list must start fresh. This needs two sequential calls,
    # so it can't be expressed as a single parametrized row.
    first = add_tag("a")
    second = add_tag("b")
    assert first == ["a"]
    assert second == ["b"]
