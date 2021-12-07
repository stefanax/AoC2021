from tools import file_handler


def part_one(is_test):
    input_array = file_handler.read_input_file_as_string_array(3, is_test)
    bits_zero = []
    bits_one = []
    input_array_string_length = len(input_array[0])-1

    for input_length in range(input_array_string_length):
        bits_zero.append(0)
        bits_one.append(0)

    for input_string in input_array:
        for input_string_pos in range(input_array_string_length):
            if int(input_string[input_string_pos]) == 1:
                bits_one[input_string_pos] += 1
            else:
                bits_zero[input_string_pos] += 1

    position_value = 1
    rate_gamma = 0
    rate_epsilon = 0
    for bits_position_invert in range(input_array_string_length):
        bits_position = input_array_string_length - 1 - bits_position_invert  #This is so we start at the end of the bits-arrays

        if bits_zero[bits_position] > bits_one[bits_position]:
            rate_epsilon += position_value
        else:
            rate_gamma += position_value

        position_value *= 2

    result = rate_gamma * rate_epsilon
    print(f'Step one: {result}')


def part_two(is_test):
    input_array_oxygen = file_handler.read_input_file_as_string_array(3, is_test)
    input_array_co2 = file_handler.read_input_file_as_string_array(3, is_test)
    input_array_string_length = len(input_array_oxygen[0]) - 1

    # Oxygen
    current_pos = 0

    while True:
        bits_zero = 0
        bits_one = 0

        for input_string in input_array_oxygen:
            if int(input_string[current_pos]) == 1:
                bits_one += 1
            else:
                bits_zero += 1

        most_common_bit = 0
        if bits_zero <= bits_one:
            most_common_bit = 1

        current_input_array_pos = len(input_array_oxygen)-1  #TODO: This is right?
        while True:
            #print(f'Meep1: {current_pos}')
            #print(f'Meep2: {input_array_oxygen[current_input_array_pos]}')
            if int(input_array_oxygen[current_input_array_pos][current_pos]) != most_common_bit:
                input_array_oxygen.pop(current_input_array_pos)
            current_input_array_pos -= 1
            if current_input_array_pos < 0:
                break

        current_pos += 1
        if current_pos > input_array_string_length-1:
            break

    # CO2
    current_pos = 0

    while True:
        bits_zero = 0
        bits_one = 0

        for input_string in input_array_co2:
            if int(input_string[current_pos]) == 1:
                bits_one += 1
            else:
                bits_zero += 1

        least_common_bit = 0
        if bits_zero > bits_one:
            least_common_bit = 1

        current_input_array_pos = len(input_array_co2) - 1  # TODO: This is right?
        while True:
            #print(f'Meep1: {current_pos}')
            #print(f'Meep2: {input_array_co2[current_input_array_pos]}')
            if int(input_array_co2[current_input_array_pos][current_pos]) != least_common_bit:
                input_array_co2.pop(current_input_array_pos)
            current_input_array_pos -= 1
            if current_input_array_pos < 0:
                break

        current_pos += 1
        if current_pos > input_array_string_length - 1:
            break
        if len(input_array_co2) == 1:
            break

    position_value = 1
    rate_oxygen = 0
    rate_co2 = 0
    for bits_position_invert in range(input_array_string_length):
        bits_position = input_array_string_length - 1 - bits_position_invert  # This is so we start at the end of the bits-arrays

        if int(input_array_oxygen[0][bits_position]) == 1:
            rate_oxygen += position_value

        if int(input_array_co2[0][bits_position]) == 1:
            rate_co2 += position_value

        position_value *= 2

    #print(rate_oxygen)

    result = rate_oxygen * rate_co2
    print(f'Step two: {result}')
