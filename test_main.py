"""
Test goes here

"""

import pandas as pd
import main

# Mock data
mock_data = {
    "employment_holes": [0, 1, 0, 1],
    "volunteer": [0, 0, 1, 1],
    "worked_during_school": [1, 1, 0, 0],
    "special_skills": [0, 0, 1, 0],
}
mock_df = pd.DataFrame(mock_data)

# Expected output based on the mock data and the results you provided
expected_output = {
    "employment_holes": {0: 2, 1: 2},
    "volunteer": {0: 2, 1: 2},
    "worked_during_school": {1: 2, 0: 2},
    "special_skills": {0: 3, 1: 1},
}


def test_check_variable():
    result = main.check_variable(mock_df)
    assert (
        result == expected_output
    ), f"Expected:\n{expected_output}\nBut got:\n{result}"


# Run the test
test_check_variable()
