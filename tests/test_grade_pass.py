import pytest
from src.grade_pass import has_passed

# 1. VALID INPUTS: Test normal scores and pass/fail boundaries (0-100)
@pytest.mark.parametrize(
    "score, expected",
    [
        (50, True),  # Minimum passing score
        (100, True), # Maximum passing score
        (75, True),  # Standard passing score
        (49, False), # Maximum failing score
        (0, False),  # Minimum failing score
    ]
)
def test_has_passed_valid(score, expected):
    # Verify the function returns the correct True/False result
    assert has_passed(score) == expected


# 2. VALUE ERROR: Test integers outside the permitted 0-100 range
@pytest.mark.parametrize(
    "score", 
    [
        -1,   # Just below minimum
        101,  # Just above maximum
        -999  # Extreme outlier
    ]
)
def test_has_passed_value_error(score):
    # Verify the function crashes with a ValueError as required
    with pytest.raises(ValueError):
        has_passed(score)


# 3. TYPE ERROR: Test invalid data types (decimals, strings, booleans, etc.)
@pytest.mark.parametrize(
    "score", 
    [
        50.5, # Float (decimal)
        "50", # String
        True, # Boolean
        None, # Missing type
        ""    # Empty string
    ]
)
def test_has_passed_type_error(score):
    # Verify the function crashes with a TypeError as required
    with pytest.raises(TypeError):
        has_passed(score)