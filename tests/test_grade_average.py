import pytest
from src.grade_average import calculate_average

# 1. VALID INPUTS: Test normal scores and boundaries (0-100)
@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0.0),       # Minimum boundary
        (100, 100, 100.0), # Maximum boundary
        (50, 51, 50.5),    # Fractional requirement
        (75, 25, 50.0)     # Standard mid-range scores
    ]
)
def test_calculate_average_valid(mark_one, mark_two, expected):
    # Verify the function returns the correct mathematical average
    assert calculate_average(mark_one, mark_two) == expected


# 2. COMBINED ERRORS: Test out-of-range values and invalid data types
@pytest.mark.parametrize(
    "mark_one, mark_two, expected_error",
    [
        # VALUE ERROR: Integers outside the permitted 0-100 range
        (-1, 50, ValueError),     # mark_one just below minimum
        (101, 50, ValueError),    # mark_one just above maximum
        (50, -1, ValueError),     # mark_two just below minimum
        (50, 101, ValueError),    # mark_two just above maximum
        
        # TYPE ERROR: Invalid data types (decimals, strings, booleans, etc.).
        (50.5, 50, TypeError),    # Float (decimal)
        ("50", 50, TypeError),    # String
        (True, 50, TypeError),    # Boolean in first parameter
        (None, 50, TypeError),    # Missing type
        (50, False, TypeError),   # Boolean in second parameter
        (50, "", TypeError)       # Empty string
    ]
)
def test_calculate_average_errors(mark_one, mark_two, expected_error):
    # Verify the function crashes with the correct specific error
    with pytest.raises(expected_error):
        calculate_average(mark_one, mark_two)