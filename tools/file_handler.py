def read_input_file_as_string_array(day, is_test):
    file_name = f'days_input/day{day}'
    if is_test:
        file_name += "_test"
    file_name += ".txt"

    with open(file_name, "r") as input_file:
        data = input_file.readlines()
    return data
