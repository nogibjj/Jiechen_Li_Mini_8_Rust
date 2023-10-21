"""
Test goes here

"""

import io
import sys
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
expected_output = """
0    2688
1    2182
Name: employment_holes, dtype: int64
=======================
0    2866
1    2004
Name: volunteer, dtype: int64
=======================
1    2725
0    2145
Name: worked_during_school, dtype: int64
=======================
0    3269
1    1601
Name: special_skills, dtype: int64
=======================
"""


def test_check_variable():
    # Capture the printed output
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    # Call the function
    main.check_variable(mock_df)

    # Get the printed output
    output = new_stdout.getvalue()
    sys.stdout = old_stdout

    # Compare the output with the expected result
    assert (
        output == expected_output
    ), f"Expected:\n{expected_output}\nBut got:\n{output}"


# Run the test
test_check_variable()
