# added comment to trigger difference to be able to merge my folders

# Ask user to input hrs and mins
# Keep asking until they enter Y (to prompt done and exit loop)
# Store the data in the format as [prompt 1], [prompt 2] .....
    # [0, 50], [1, 20], [3, 5]       [hrs, min]


def get_user_input():
    # create a list
    times_list = []
    user_input_1 = 0
    while (user_input_1 != 'Y'):
            user_input_1 = input("Enter the hour(s)   or enter 'Y' if you're done: ")
            if (user_input_1 or user_input_2) == 'Y':
                return f"Displays time  list: {times_list} "

            user_input_2 = input("Enter the minute(s):      ")

            int_user_input_1 = int(user_input_1)
            int_user_input_2 = int(user_input_2)

            try:
                if user_input_2 >= 60:
                    print("Please enter the value again")
            except:
                print("input: ")

            time = [int_user_input_1, ]
            print(time)
            times_list += [time]
            print(times_list)

get_user_input()

# shouldn't accept input2(minutes) to be greater than 59


    # [0, 50]
# other possible test cases in which it breaks. if they enter 0 hrs, 180 minutes. Does this cause it to break? or does it convert to 3hrs?

# another possible scenario is the user gives a blank input. Should handle the value as 0 or ask them to reenter value

def time_list_creator(hr, min):
    """Create a list of hr and min

    :param hr: hour
    :param min: minute

    :return: list - hr and minute integer value.
    """
    # If minute paramater is greater than 59, create an empty list

    # change this so it's interactive. Gets input from prompt

    # int_hr = int(hr)
    # int_min = int(min)
    # # print(int_hr)
    # # print(int_min)

    if int_min <= 59:
        # create the list
        hr_min = [int_hr, int_min]
        # print([int_hr, int_min])
        return [int_hr, int_min]


def check_min_greater_than_59(minutes):
    """ Checks if the minutes is greater than 59. Converts it into hrs and minutes if it is.

    :param minutes: int- value of minutes
    :return: list - hrs and minutes [1, 15]

    If it is, it converts it into __hrs __ min
    """
    # if it isn't greater than 59, return [0, min] #=> [0, 59]

    # 1. convert minutes into integer
    int_min = int(minutes)
    # 2. check if if minutes is greater than 59:
    print("checking check min greater than 59.")
    if int_min > 59:
        # Get hrs: divide it by 60.
        hrs = int_min//60
        # Get min: value of %60
        mins = int_min % 60
        # print(hrs)
        # print(mins)
        # print([hrs, mins])
        # print("its greater than 59")
        return [hrs, mins]

    else:
        # print([0, int_min])
        # print("its less than 59")
        return [0, int_min]
# check_min_greater_than_59(75)
# check_min_greater_than_59(35)


# convert minutes into hrs + min
# check_min_greater_than_59(75) #=> [1, 15] 1hr 15min
# check_min_greater_than_59(34) #=> [0, 34] 0hr 34 min

def display_as_string(time):
    """ Displays a list [1,24] as a string
    E.g. "1hr 24min"

    :param time: list containing hr and minute
    :returns: string - total time as a string "__hrs __mins"
    """
    string_total= f"Total time: {time[0]}hrs {time[1]}minute(s)"
    # print(string_total)
    print("checking dispaly_as_string.")
    return string_total


def time_adder(list_of_times):
    """Takes a list of times, and returns the total time

    :param list_of_times: list containing int times
    :returns: string - total of time as a string
    """
    sum_hrs = 0
    sum_mins = 0
    for time in list_of_times:
        hrs = time[0]
        sum_hrs += hrs

        mins = time[1]
        sum_mins += mins

    total_mins = (check_min_greater_than_59(sum_mins))

    total_hrs = sum_hrs

    if total_mins[0] > 0:
        # add all the hours again
        total_hrs = total_mins[0] + sum_hrs # this is the hrs for the final output
        # print(total_hrs, "result of min_in_hrs_total") # gets hours
        # print(total_mins[1], "result of: total_mins[1]") # gets minutes

    total_list = [total_hrs, total_mins[1]]
    print(display_as_string(total_list))
    return display_as_string(total_list)

    print("checking time_adder")


time_adder([[0,55],[0,33],[1,50]])


# format we need to store data time_adder([[0,55],[0,33],[0,50]])

# [0, 55], [0,33], [0,50]
