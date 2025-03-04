'''
for a time calculator what is the unit test?
making sure each function works as intended.
    E.g. each prompt
    The total of the added numbers are correct. (e.g. the output from adding the list)

Functional testing would be something like if you have multiple functions, it should work as intended
    E.g. Between two unit tests ((1)input prompt, (2)then using the input prompt to create a list which adds everything together)

    Another example would be: if you have substraction involved. You can add times, then you can substract times. A function test will involve adding things together and then substracting it.

TLDR:
    Unit test for:
        1. Input Function (input - checking the input is valid)
        2. Time Addition (the logic)
        3. Time Substraction (the logic)
    Functional test for:
        1. Input + addtion
        2. Input + substraction
        3. Input + addition + substraction
'''


'''
Unit Tests for time_adder.py
- Unit tests will check that all my functions work as intended

Unit tests include:
    1. time_list_creator - what do I need to test exactly?
        - The output should always return a list in the format of [[1,10],[3, 35], [5,17]]
        output: always a list
        - items in each list within the list should ONLY be integers

    2. check_min_greater_than_59(minutes)
        - should always return a list in one of the following formats:
            2.1 [0, 59]
            2.2 [0, 70] => [1, 10]
        - the minutes value when returned should never exceed 59. (0-59 are valid values when returned)

    3. display_as_string(time)
        - should always display as a string:
            Total time: __ hrs __ minute(s).

    4. time_adder(list_of_times)
        - should get the numbers and the output should return the total hrs and minutes. e.g 4hrs 30min
    !! We still need to check the logic for time_adder is correct
'''
