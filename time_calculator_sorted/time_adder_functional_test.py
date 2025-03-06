from unittest.mock import patch
from time_adder import time_list_creator, get_inputs, check_min_greater_than_59, display_as_string, time_adder

# Create a functional test
# A functional test is going to test everything from start to end
"""
Flow is the following:
1. time_list_creator => 2. check_min_greater_than_59(minutes)
3. display_as_string(time)
4. time_adder(list_of_times)
"""

def test_time_adder_functionality():
    # Use mock to simulate user input
    with patch('time_adder.input', side_effect=["1", "50", "2", "10", "3", "15", "q"]):
        time_list = time_list_creator(get_inputs)
        added_time = time_adder(time_list)

        assert added_time == "Total time: 7hrs 15minute(s)"

        # all the tests I need are:
        # time_list_creator

    # only test list_time_creator and time_adder



    # should have code in between to run the whole thing so all the codes work together
    # assert time_list_creator() == #expected output

    # assert check_min_greater_than_59(minutes) == #expected output

    # assert display_as_string(time) == #expected output

    # assert time_adder(list_of_times) == #expected output


    # don't need to test for check_min_greater_than_59(minutes) and display_as_string(time) because they're used in the time_adder funciton.

def test_time_adder_two_inputs_functionality():
    # Use mock to simulate user input
    with patch('time_adder.input', side_effect=["3", "30", "1", "5", "q"]):
        time_list = time_list_creator(get_inputs)
        added_time = time_adder(time_list)

        assert added_time == "Total time: 4hrs 35minute(s)"

def test_time_adder_edge_case_1_functionality():
    # Use mock to simulate user input
    with patch('time_adder.input', side_effect=["0", "0", "0", "59", "q"]):
        time_list = time_list_creator(get_inputs)
        added_time = time_adder(time_list)

        assert added_time == "Total time: 0hrs 59minute(s)"

def test_time_adder_edge_case_2_functionality():
    # Use mock to simulate user input
    with patch('time_adder.input', side_effect=["0", "1", "0", "59", "q"]):
        time_list = time_list_creator(get_inputs)
        added_time = time_adder(time_list)

        assert added_time == "Total time: 1hrs 0minute(s)"
