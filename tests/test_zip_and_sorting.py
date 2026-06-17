import pytest

from exercises.zip_and_sorting import combine, top_scorers


@pytest.mark.parametrize(
    "words, nums, expected",
    [
        (["alice", "bob"], [90, 85], {"alice": 90, "bob": 85}),
        ([], [], {}),
    ],
)
def test_combine(words, nums, expected):
    assert combine(words, nums) == expected


def test_combine_raises_on_length_mismatch():
    # zip(..., strict=True) must reject unequal lengths. This is a single
    # exception scenario, not a table of values, so a plain test reads better
    # than parametrize.
    with pytest.raises(ValueError):
        combine(["alice"], [90, 85])


@pytest.mark.parametrize(
    "scores, expected",
    [
        (
            [("alice", 90), ("bob", 85), ("carol", 95)],
            [("carol", 95), ("alice", 90), ("bob", 85)],
        ),
        ([], []),
    ],
)
def test_top_scorers(scores, expected):
    assert top_scorers(scores) == expected
