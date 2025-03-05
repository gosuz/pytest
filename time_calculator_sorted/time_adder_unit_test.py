# from unittest.mock import patch
# from time_adder import time_list_creator, check_min_greater_than_59, display_as_string, time_adder, get_inputs

from unittest.mock import patch
from time_adder import time_list_creator, get_inputs, check_min_greater_than_59

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





    # needs to test what?? what is the unit test? is it going to check that if it's 59,it's going to be return [0, int_min]
    # and if its less than 59 it would return [hrs, mins]
