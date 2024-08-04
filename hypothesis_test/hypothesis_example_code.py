from hypothesis import given, strategies as st

# Function to test
def process_input(value):
    if not isinstance(value, str):
        raise ValueError('Input must be a string')
    return value.lower()

# Hypothesis test
@given(st.text())
def test_process_input(value):
    result = process_input(value)
    assert isinstance(result, str)
    assert result == value.lower()

# Run the test
test_process_input()
