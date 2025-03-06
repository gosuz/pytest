# from unittest.mock import patch
# from time_adder import time_list_creator, check_min_greater_than_59, display_as_string, time_adder, get_inputs
import pytest
from unittest.mock import patch
from time_adder import time_list_creator, get_inputs, check_min_greater_than_59, display_as_string, time_adder

# unit tests for time adder
'''
4 things to test:
    1. time_list_creator()
    2. check_min_greater_than_59(minutes)
    3. display_as_string(time)
    4. time_adder(list_of_times)
'''

# create unit test for time_list_creator
def test_time_list_creator():
    # Use mock to simulate user input
    with patch('time_adder.input', side_effect=["1", "50", "2", "10", "3", "15", "q"]):
        result = time_list_creator(get_inputs)  # This calls time_list_creator and indirectly get_inputs
    assert result == [[1, 50], [2, 10], [3, 15]]


# create unit test for check_min_greater_than_59(minutes)
def test_check_min_greater_than_59():
    assert check_min_greater_than_59("15") == [0, 15]
    assert check_min_greater_than_59("25") == [0, 25]
    assert check_min_greater_than_59("59") == [0, 59]
    assert check_min_greater_than_59("75") == [1, 15]
    assert check_min_greater_than_59("90") == [1, 30]

    # edge cases
    assert check_min_greater_than_59("60") == [1, 0]
    assert check_min_greater_than_59("61") == [1, 1]
    assert check_min_greater_than_59("0") == [0, 0]

def test_display_as_string():
    # cases that should always pass
    assert display_as_string([1, 20]) == "Total time: 1hrs 20minute(s)"
    assert display_as_string([0, 50]) == "Total time: 0hrs 50minute(s)"
    assert display_as_string([2, 15]) == "Total time: 2hrs 15minute(s)"

    # edge cases
    assert display_as_string([0, 59]) == "Total time: 0hrs 59minute(s)"
    assert display_as_string([1, 0]) == "Total time: 1hrs 0minute(s)"
    assert display_as_string([0, 0]) == "Total time: 0hrs 0minute(s)"

# create test for time_adder()
def test_time_adder():
    assert time_adder([[0,10],[0,20]]) == "Total time: 0hrs 30minute(s)"
    assert time_adder([[1,30],[0,15]]) == "Total time: 1hrs 45minute(s)"
    assert time_adder([[2,55],[0,5]]) == "Total time: 3hrs 0minute(s)"
    assert time_adder([[2,55],[0,5],[1,5]]) == "Total time: 4hrs 5minute(s)"



    # edge cases
    assert time_adder([[0,1],[0,59]]) == "Total time: 1hrs 0minute(s)"
    assert time_adder([[0,1],[0,60]]) == "Total time: 1hrs 1minute(s)"
