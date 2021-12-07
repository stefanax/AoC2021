from tools import file_handler


def part_one(is_test):
    input_array = file_handler.read_input_file_as_string_array(2, is_test)
    pos_x = 0
    pos_y = 0

    for input_string in input_array:
        command = input_string.split(" ")[0]
        steps = int(input_string.split(" ")[1])

        if command == "forward":
            pos_x += steps
        elif command == "up":
            pos_y -= steps
        elif command == "down":
            pos_y += steps

    result = pos_x * pos_y
    print(f'Step one: {result}')


def part_two(is_test):
    input_array = file_handler.read_input_file_as_string_array(2, is_test)
    pos_x = 0
    pos_y = 0
    aim = 0

    for input_string in input_array:
        command = input_string.split(" ")[0]
        steps = int(input_string.split(" ")[1])

        if command == "forward":
            pos_x += steps
            pos_y += aim * steps
        elif command == "up":
            aim -= steps
        elif command == "down":
            aim += steps

    result = pos_x * pos_y
    print(f'Step two: {result}')
