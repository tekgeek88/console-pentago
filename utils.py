import math


def convert_2d_array_to_2d_tuple(array):
    for i in range(len(array)):
        array[i] = tuple(array[i])
    return tuple(array)


def convert_2d_tuple_to_2d_array(tuple_to_convert):
    result_list = list(tuple_to_convert)
    for i in range(len(tuple_to_convert)):
        result_list[i] = list(tuple_to_convert[i])
    return list(result_list)


def get_2d_point(index):
    return math.floor((index-1) % 3), (index-1) // 3


def print_pretty_tile(state, tile_number):
    tile_tuple = state[tile_number - 1]
    for i in range(len(tile_tuple)):
        for j in range(len(tile_tuple)):
            print(tile_tuple[i][j], end=" ")
        print()


def print_pretty_board(state):
    line_width = 15
    print("+", end="")
    for i in range(line_width):
        if (i + 1) % 8 == 0:
            print("+", end="")
        else:
            print("-", end="")
    print("+", end="")
    print()
    for row in range(6):
        for column in range(6):
            if column == 0:
                print("| ", end="")
            board_number = get_tile_number((column, row)) - 1
            board_char = "{:>1}".format(state[board_number][row % 3][column % 3])
            print(board_char.format(), end=" ")
            if (column+1) % 3 == 0:
                print("| ", end="")
        print()
        if (row+1) % 3 == 0:
            print("+", end="")
            for i in range(line_width):
                if (i + 1) % 8 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print("+", end="")
            print()


def get_tile_number(point_tuple):
    x, y = point_tuple
    board_number = 0

    if y < 3:
        if x < 3:
            board_number = 1
        else:
            board_number = 2
    else:
        if x < 3:
            board_number = 3
        else:
            board_number = 4

    return board_number


def get_board_row_column(tuple_x_y):
    result = get_tile_number(tuple_x_y) -1, tuple_x_y[1] % 3, tuple_x_y[0] % 3
    return result


def is_neighbor(move_tuple):
    get_2d_point(move_tuple[1])


def sort_actions_player_left_or_right(actions: list, piece_list, player):
    pass
    # sorted_actions = [x for x in actions if not is_neighbor(x)]


def get_neighbors(x, y):
    neighbor_list = list()
    # Get north neighbor
    if y > 0:
        neighbor_list.append(get_board_row_column((x, y-1)))
    # get east_neighbor
    if x < 5:
        neighbor_list.append(get_board_row_column((x+1, y)))
    # get south neighbor
    if y < 5:
        neighbor_list.append(get_board_row_column((x, y + 1)))
    # get west neighbor
    if x > 0:
        neighbor_list.append(get_board_row_column((x-1, y)))
    return neighbor_list

