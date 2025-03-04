# from unittest.mock import patch
# from time_adder import time_list_creator, check_min_greater_than_59, display_as_string, time_adder, get_inputs

from unittest.mock import patch
from time_adder import time_list_creator, get_inputs

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
