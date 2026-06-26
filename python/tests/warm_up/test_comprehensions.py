import pytest

from exercises.warm_up.comprehensions import square_odds, sum_evens, word_lengths


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5, 6], 12),
        ([1, 3, 5], 0),
        ([], 0),
    ],
)
def test_sum_evens(numbers, expected):
    assert sum_evens(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5], [1, 9, 25]),
        ([2, 4, 6], []),
        ([], []),
    ],
)
def test_square_odds(numbers, expected):
    assert square_odds(numbers) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["hi", "hello", "hey"], {"hi": 2, "hello": 5, "hey": 3}),
        ([], {}),
    ],
)
def test_word_lengths(words, expected):
    assert word_lengths(words) == expected
