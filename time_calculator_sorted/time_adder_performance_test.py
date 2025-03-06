import pytest
from unittest.mock import patch
from time_adder import time_list_creator, get_inputs, check_min_greater_than_59, display_as_string, time_adder

# create performance test with different inputs

# use @pytest.mark.parametrize for setting up multiple inputs
    # create inputs for 2~5 inputs using parametrize.
    # the testing is for the whole function (time_adder())

# use @pytest.mark.benchmark for measuring time

# create sample input data using parametrize
@pytest.mark.parametrize("sample_input, expected_time_list, expected_output", [
    # 2 , 3, 4, 5 inputs
    (["2", "5", "4", "25"],[[2, 5], [4, 25]], "Total time: 6hrs 30minute(s)"),
    (["2", "5", "4", "25", "1", "12"],[[2, 5], [4, 25], [1, 12]],"Total time: 7hrs 42minute(s)"),
    (["2", "5", "4", "25", "1", "12", "1", "28", "0", "2"],[[2, 5], [4, 25],[1, 12], [1, 28], [0, 2]], "Total time: 9hrs 12minute(s)"),
    (["2", "5", "4", "25", "1", "12", "1", "28", "0", "2", "0","70"],[[2, 5], [4, 25],[1, 12], [1, 28], [0, 2], [0,70]], "Total time: 10hrs 22minute(s)")
    # add a test case later e.g. [0, 70]
])

# use benchmark to see how long it takes to calcualte each input
# the group is the name of the test. we label it so we can refer to the test later much easier
@pytest.mark.benchmark(group="time_adder_performance")
def test_performance_test(sample_input, expected_time_list, expected_output, benchmark):
    with patch('time_adder.input', side_effect=sample_input + ["q"]):
        time_list = time_list_creator(get_inputs)
        result = benchmark(time_adder, time_list)

    # what do I want to check? assert what???
    # check the time_list is correct
    assert time_list == expected_time_list

    # check the result (time_adder() actually is correct)
    assert result == expected_output

# the expected output isn't going to be the expected output. the expecte output changes for each thing
