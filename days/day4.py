from tools import file_handler


def part_one(is_test):
    input_array = file_handler.read_input_file_as_string_array(4, is_test)

    input_numbers = input_array[0].strip().split(",")
    game_boards = []
    game_board_markers = []

    input_array_pos = 2
    while True:
        game_board_markers.append([[False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False]])

        game_board = []
        for counter in range(0, 5):
            input_array_row = input_array[input_array_pos + counter]
            temp_row = [int(input_array_row[0:2].strip()),
                        int(input_array_row[3:5].strip()),
                        int(input_array_row[6:8].strip()),
                        int(input_array_row[9:11].strip()),
                        int(input_array_row[12:14].strip())]
            game_board.append(temp_row)
        game_boards.append(game_board)

        input_array_pos += 6
        if input_array_pos >= len(input_array):
            break

    winning_board = -1
    for input_number_pos in range(0, len(input_numbers)):
        input_number = int(input_numbers[input_number_pos])

        for game_board_pos in range(0, len(game_boards)):
            game_board = game_boards[game_board_pos]
            game_board_marker = game_board_markers[game_board_pos]
            for game_board_y in range(0, 5):
                for game_board_x in range(0, 5):
                    if game_board[game_board_y][game_board_x] == input_number:
                        game_board_marker[game_board_y][game_board_x] = True
                        if (game_board_marker[game_board_y][0] and game_board_marker[game_board_y][1] and
                                game_board_marker[game_board_y][2] and game_board_marker[game_board_y][3] and
                                game_board_marker[game_board_y][4]):
                            winning_board = game_board_pos
                        if (game_board_marker[0][game_board_x] and game_board_marker[1][game_board_x] and
                                game_board_marker[2][game_board_x] and game_board_marker[3][game_board_x] and
                                game_board_marker[4][game_board_x]):
                            winning_board = game_board_pos
            if winning_board != -1:
                break
        if winning_board != -1:
            break

    total_amount = 0
    for game_board_y in range(0, 5):
        for game_board_x in range(0, 5):
            if not game_board_markers[winning_board][game_board_y][game_board_x]:
                total_amount += game_boards[winning_board][game_board_y][game_board_x]

    result = total_amount * input_number
    print(f'Step one: {result}')


def part_two(is_test):
    input_array = file_handler.read_input_file_as_string_array(4, is_test)

    input_numbers = input_array[0].strip().split(",")
    game_boards = []
    game_board_markers = []

    input_array_pos = 2
    while True:
        game_board_markers.append([[False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False],
                                  [False, False, False, False, False]])

        game_board = []
        for counter in range(0, 5):
            input_array_row = input_array[input_array_pos + counter]
            temp_row = [int(input_array_row[0:2].strip()),
                        int(input_array_row[3:5].strip()),
                        int(input_array_row[6:8].strip()),
                        int(input_array_row[9:11].strip()),
                        int(input_array_row[12:14].strip())]
            game_board.append(temp_row)
        game_boards.append(game_board)

        input_array_pos += 6
        if input_array_pos >= len(input_array):
            break

    winning_board = -1
    for input_number_pos in range(0, len(input_numbers)):
        input_number = int(input_numbers[input_number_pos])

        for game_board_pos in range(0, len(game_boards)):
            redo_check = True
            while redo_check:
                redo_check = False
                if len(game_boards) <= game_board_pos:
                    break
                game_board = game_boards[game_board_pos]
                game_board_marker = game_board_markers[game_board_pos]
                for game_board_y in range(0, 5):
                    for game_board_x in range(0, 5):
                        if game_board[game_board_y][game_board_x] == input_number:
                            game_board_marker[game_board_y][game_board_x] = True
                            if (game_board_marker[game_board_y][0] and game_board_marker[game_board_y][1] and
                                    game_board_marker[game_board_y][2] and game_board_marker[game_board_y][3] and
                                    game_board_marker[game_board_y][4]):
                                if len(game_boards) == 1:
                                    winning_board = 1
                                    break
                                else:
                                    game_boards.pop(game_board_pos)
                                    game_board_markers.pop(game_board_pos)
                                    redo_check = True
                            if (game_board_marker[0][game_board_x] and game_board_marker[1][game_board_x] and
                                    game_board_marker[2][game_board_x] and game_board_marker[3][game_board_x] and
                                    game_board_marker[4][game_board_x]):
                                if len(game_boards) == 1:
                                    winning_board = 1
                                    break
                                else:
                                    game_boards.pop(game_board_pos)
                                    game_board_markers.pop(game_board_pos)
                                    redo_check = True
                    if winning_board != -1:
                        break
            if winning_board != -1:
                break
        if winning_board != -1:
            break

    total_amount = 0
    for game_board_y in range(0, 5):
        for game_board_x in range(0, 5):
            if not game_board_markers[0][game_board_y][game_board_x]:
                total_amount += game_boards[0][game_board_y][game_board_x]

    result = total_amount * input_number
    print(f'Step two: {result}')
