from logic_utils import check_guess
import pytest
from logic_utils import (
    check_guess,
    parse_guess,
    get_range_for_difficulty,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"



# --- Tests for check_guess ---

def test_winning_guess():
    assert check_guess(50, 50) == "Win"


def test_guess_too_high():
    assert check_guess(75, 50) == "Too High"


def test_guess_too_low():
    assert check_guess(25, 50) == "Too Low"


# --- Tests for parse_guess ---

def test_parse_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None


def test_parse_float_string():
    ok, val, err = parse_guess("42.0")
    assert ok is True
    assert val == 42
    assert err is None


def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert err == "Enter a guess."


def test_parse_invalid_text():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert val is None
    assert err == "That is not a number."


# --- Tests for get_range_for_difficulty ---

@pytest.mark.parametrize(
    "difficulty, expected_low, expected_high",
    [
        ("Easy", 1, 20),
        ("Normal", 1, 100),
        ("Hard", 1, 200),
        ("Unknown", 1, 100),
    ],
)
def test_get_range_for_difficulty(difficulty, expected_low, expected_high):
    low, high = get_range_for_difficulty(difficulty)
    assert low == expected_low
    assert high == expected_high


# --- Tests for update_score ---

def test_update_score_win():
    # Winning on 1st attempt: 100 - 10*(1-1) = 100 pts added
    assert update_score(0, "Win", attempt_number=1) == 100


def test_update_score_incorrect_guess():
    # Incorrect guess deducts 5 points
    assert update_score(50, "Too High", attempt_number=1) == 45
    assert update_score(50, "Too Low", attempt_number=2) == 45