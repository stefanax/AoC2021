from tools import file_handler


def part_one(is_test):
    input_array = file_handler.read_input_file_as_string_array(1, is_test)
    increase_count = 0
    for input_string_pos in range(1, len(input_array)):
        if int(input_array[input_string_pos-1]) < int(input_array[input_string_pos]):
            increase_count += 1

    print(f'Count of increases: {increase_count}')


def part_two(is_test):
    input_array = file_handler.read_input_file_as_string_array(1, is_test)
    increase_count = 0
    for input_string_pos in range(3, len(input_array)):
        if int(input_array[input_string_pos-3]) < int(input_array[input_string_pos]):
            increase_count += 1

    print(f'Count of increases: {increase_count}')
