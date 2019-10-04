import game as g
import utils
import utility
import player as p
import board as b

game = g.Problem()

player_01 = p.Player("Carl", "W", "Human")
player_02 = p.Player("Luke", "B", "Human")

game.add_player(player_01)
game.add_player(player_02)

print()
print(f"Player 1: {player_01}")
print(f"Player 2: {player_02}")


def utility_line_test_horizontal_all_max():
    lines = []
    lines.append(['W', '.', '.', '.', '.'])
    lines.append(['W', 'W', '.', '.', '.'])
    lines.append(['W', 'W', 'W', '.', '.'])
    lines.append(['W', 'W', 'W', 'W', '.'])
    lines.append(['W', 'W', 'W', 'W', 'W'])
    lines.append(['.', 'W', 'W', 'W', 'W'])
    lines.append(['.', '.', 'W', 'W', 'W'])
    lines.append(['.', '.', '.', 'W', 'W'])
    lines.append(['.', '.', '.', '.', 'W'])
    lines.append(['.', '.', '.', '.', '.'])
    lines.append(['.', 'W', '.', '.', '.'])
    lines.append(['.', '.', 'W', '.', '.'])
    lines.append(['.', '.', '.', 'W', '.'])
    lines.append(['.', 'W', 'W', '.', '.'])
    lines.append(['.', '.', 'W', 'W', '.'])
    lines.append(['W', 'W', '.', 'W', 'W'])
    lines.append(['W', '.', 'W', '.', 'W'])
    lines.append(['W', 'W', '.', '.', 'W'])
    lines.append(['W', 'W', 'W', 'B', 'W'])


    for line in lines:
        print(f"Line: {line}, Utility: {utility.utility_in_line(line, player_01, True)}")

    print("finished test")


def utility_line_test_max_and_min():
    lines = []
    lines.append(['W', '.', '.', '.', 'B'])
    lines.append(['W', 'W', '.', 'B', '.'])
    lines.append(['W', 'W', 'B', '.', '.'])
    lines.append(['W', 'B', 'W', 'W', '.'])
    lines.append(['B', 'W', 'W', 'W', 'W'])
    lines.append(['B', 'W', 'W', 'W', 'W'])
    lines.append(['B', '.', 'W', 'W', 'W'])
    lines.append(['.', '.', '.', 'W', 'B'])
    lines.append(['.', '.', '.', 'B', 'W'])
    lines.append(['.', '.', '.', '.', 'B'])
    lines.append(['B', 'W', '.', '.', '.'])
    lines.append(['.', 'B', 'W', 'B', '.'])


    for line in lines:
        print(f"Line: {line}, Utility: {utility.utility_in_line(line, player_01, True)}")

    print("finished test")


def horizontal_left_utility_test():
    # Horizontal
    tile_01 = (
        ('W', 'W', 'W'),
        ('.', '.', '.'),
        ('.', 'W', '.')
    )

    tile_02 = (
        ('B', 'W', 'W'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', '.', '.'),
        ('W', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('W', '.', '.'),
        ('W', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("horizontal_left_utility_test:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_horizontal_left(game.get_state())
    total_utility = 0
    utility_val = utility.utility_in_lines(lines, player_01, True)
    print(utility_val)

    print("finished test")



def horizontal_right_utility_test():
    # Horizontal
    tile_01 = (
        ('W', 'W', 'W'),
        ('.', '.', '.'),
        ('.', 'W', '.')
    )

    tile_02 = (
        ('B', 'W', 'W'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', '.', '.'),
        ('W', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('W', '.', '.'),
        ('W', '.', 'W')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("horizontal_right_utility_test:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_horizontal_right(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def horizontal_left_and_right_utility_test():
    # Horizontal
    tile_01 = (
        ('W', 'W', 'W'),
        ('.', '.', '.'),
        ('.', 'W', '.')
    )

    tile_02 = (
        ('B', 'W', 'W'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', '.', '.'),
        ('W', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('W', '.', '.'),
        ('W', '.', 'W')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("horizontal_left and right_utility_test:")
    utils.print_pretty_board(game.get_state())
    current_utility = utility._utility_horizontal(game.get_state(), player_01, True)
    print(f"Utility: {current_utility}")

    print("finished test")


def vertical_top_utility_test():
    # Horizontal
    tile_01 = (
        ('W', '.', '.'),
        ('W', 'W', '.'),
        ('W', 'W', 'W')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('W', 'W', 'W'),
        ('W', 'W', 'W'),
        ('.', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', 'W'),
        ('.', '.', 'W')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("vertical_top_utility_test:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_vertical_top(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def vertical_bottom_utility_test():
    # Horizontal
    tile_01 = (
        ('W', '.', '.'),
        ('W', 'W', '.'),
        ('W', 'W', 'W')
    )

    tile_02 = (
        ('.', '.', 'W'),
        ('.', '.', 'W'),
        ('.', '.', 'W')
    )

    tile_03 = (
        ('W', 'W', 'W'),
        ('W', 'W', 'W'),
        ('.', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', 'W'),
        ('.', '.', 'W')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("vertical_bottom_utility_test:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_vertical_bottom(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_left_lowerband():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('W', '.', '.'),
        ('.', 'W', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('W', '.', '.'),
        ('.', 'W', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("utility_lines_diagonal_left_lowerband:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_left_lowerband(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_left_upperband():
    # Horizontal
    tile_01 = (
        ('.', 'W', '.'),
        ('.', '.', 'W'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('W', '.', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', 'W', '.'),
        ('.', '.', 'W'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_left_upper:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_left_upperband(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_left_centerband_upper():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', 'W', '.'),
        ('.', '.', 'W')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('W', '.', '.'),
        ('.', 'W', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_left_centerband_upper:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_left_centerband_upper(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_left_centerband_lower():
    # Horizontal
    tile_01 = (
        ('B', '.', '.'),
        ('.', 'W', '.'),
        ('.', '.', 'W')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('W', '.', '.'),
        ('.', 'W', '.'),
        ('.', '.', 'B')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_left_centerband_lower:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_left_centerband_lower(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_right_lowerband():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', 'W'),
        ('.', 'W', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', 'W'),
        ('.', 'W', '.')
    )

    tile_04 = (
        ('W', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_right_lowerband:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_right_lowerband(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_right_upperband():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', 'W')
    )

    tile_02 = (
        ('.', 'W', '.'),
        ('W', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', 'W', '.'),
        ('W', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_right_centerband_upper:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_right_upperband(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_right_centerband_upper():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', 'W'),
        ('.', 'W', '.'),
        ('W', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', 'W', '.'),
        ('B', '.', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_right_centerband_upper:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_right_centerband_upper(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


def utility_lines_diagonal_right_centerband_lower():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', 'W', '.'),
        ('W', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'W'),
        ('.', 'W', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("_utility_lines_diagonal_right_centerband_lower:")
    utils.print_pretty_board(game.get_state())
    lines = utility._get_lines_diagonal_right_centerband_lower(game.get_state())
    total_utility = 0
    for line in lines:
        current_utility = utility.utility_in_line(line, player_01, True)
        total_utility += current_utility
        print(f"Line: {line}, Utility: {current_utility}")

    print("finished test")


########################################################
#                   Main Program
########################################################


if __name__ == '__main__':

    # New utility tests here
    utility_line_test_horizontal_all_max()
    # utility_line_test_max_and_min()
    # horizontal_left_utility_test()
    # horizontal_right_utility_test()
    # horizontal_left_and_right_utility_test()
    # vertical_top_utility_test()
    # vertical_bottom_utility_test()
    # utility_lines_diagonal_left_lowerband()
    # utility_lines_diagonal_left_upperband()
    # utility_lines_diagonal_left_centerband_upper()
    # utility_lines_diagonal_left_centerband_lower()
    # utility_lines_diagonal_right_lowerband()
    # utility_lines_diagonal_right_upperband()
    # utility_lines_diagonal_right_centerband_upper()
    # utility_lines_diagonal_right_centerband_lower()