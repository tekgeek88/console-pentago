import game as g
import utils
import player as p
import board as b

game = g.Problem()

player1 = p.Player("Carl", "B", "Human")
player2 = p.Player("Luke", "W", "Human")

game.add_player(player1)
game.add_player(player2)

print()
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")


def tile_location_test():
    board_01 = (
        ('1_1', '1_2', '1_3'),
        ('1_4', '1_5', '1_6'),
        ('1_7', '1_8', '1_9')
    )

    board_02 = (
        ('2_1', '2_2', '2_3'),
        ('2_4', '2_5', '2_6'),
        ('2_7', '2_8', '2_9')
    )

    board_03 = (
        ('3_1', '3_2', '3_3'),
        ('3_4', '3_5', '3_6'),
        ('3_7', '3_8', '3_9')
    )

    board_04 = (
        ('4_1', '4_2', '4_3'),
        ('4_4', '4_5', '4_6'),
        ('4_7', '4_8', '4_9')
    )


    board = b.Board(board_01, board_02, board_03, board_04)
    game.set_board(board)
    game.set_state(board.get_board_state())

    print()
    print("tile_location_test")
    utils.print_pretty_board(game.get_state())
    print()

    print("Display Horizontal Map:")
    for row in range(3):
        print(f"Row: {row}")
        i = 2
        j = 0
        while i >= 0 and j <= 2:
            print(f"{board_01[row][i]}, {board_02[row][j]}")
            i -= 1
            j += 1


def solution_horizontal_test():
    # Test for horizontal winners
    tile_01 = (
        ('.', '.', '.'),
        ('B', 'B', 'B'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('B', 'B', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', 'W', 'W')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('W', 'W', 'W')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())

    print()
    print("solution_horizontal_test:")
    utils.print_pretty_board(game.get_state())
    print()
    print("Horizontal Tests:")
    print(f"Player1 winner: {g._is_solution_horizontal(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_horizontal(game.get_state(), player2)}")


def solution_vertical_test():
    # Test for horizontal winners
    tile_01 = (
        ('B', '.', '.'),
        ('B', '.', '.'),
        ('B', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', 'W', '.'),
        ('.', 'W', '.')
    )

    tile_03 = (
        ('B', '.', '.'),
        ('B', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', 'W', '.'),
        ('.', 'W', '.'),
        ('.', 'W', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())

    print()
    print("solution_vertical_test:")
    utils.print_pretty_board(game.get_state())
    print()
    print("Vertical Tests:")
    print(f"Player1 winner: {g._is_solution_vertical(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_vertical(game.get_state(), player2)}")


def solution_left_diagonal_center_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('B', '.', '.'),
        ('.', 'B', '.'),
        ('.', '.', 'B')
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
        ('B', '.', '.'),
        ('.', 'B', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("Diagonal Center-band Tests:")
    utils.print_pretty_board(game.get_state())
    print(f"Player1 winner: {g._is_solution_diagonal_left(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_left(game.get_state(), player2)}")

def solution_left_diagonal_lower_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('.', '.', '.'),
        ('B', '.', '.'),
        ('.', 'B', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'B'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('B', '.', '.'),
        ('.', 'B', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("Diagonal Center-band Tests:")
    utils.print_pretty_board(game.get_state())

    print()
    print("Diagonal Lower-band Tests:")
    print(f"Player1 winner: {g._is_solution_diagonal_left(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_left(game.get_state(), player2)}")

def solution_left_diagonal_upper_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('.', 'B', '.'),
        ('.', '.', 'B'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('B', '.', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_04 = (
        ('.', 'B', '.'),
        ('.', '.', 'B'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("Left Diagonal Upper-band Tests:")
    utils.print_pretty_board(game.get_state())

    print()
    print("Diagonal Upper-band Tests:")
    print(f"Player1 winner: {g._is_solution_diagonal_left(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_left(game.get_state(), player2)}")


def solution_right_diagonal_center_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', 'B'),
        ('.', 'B', '.'),
        ('B', '.', '.')
    )

    tile_03 = (
        ('.', '.', 'B'),
        ('.', 'B', '.'),
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
    print("Diagonal Center-band Tests:")
    utils.print_pretty_board(game.get_state())
    print(f"Player1 winner: {g._is_solution_diagonal_right(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_right(game.get_state(), player2)}")

def solution_right_diagonal_lower_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('.', '.', '.'),
        (',', '.', '.'),
        ('.', '.', '.')
    )

    tile_02 = (
        ('.', '.', '.'),
        ('.', '.', 'B'),
        ('.', 'B', '.')
    )

    tile_03 = (
        ('.', '.', '.'),
        ('.', '.', 'B'),
        ('.', 'B', '.')
    )

    tile_04 = (
        ('B', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("Diagonal Center-band Tests:")
    utils.print_pretty_board(game.get_state())

    print()
    print("Diagonal Lower-band Tests:")
    print(f"Player1 winner: {g._is_solution_diagonal_right(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_right(game.get_state(), player2)}")

def solution_right_diagonal_upper_band_test():
    # Test for horizontal winners
    tile_01 = (
        ('W', 'W', 'W'),
        ('W', 'W', '.'),
        ('.', 'W', 'W')
    )

    tile_02 = (
        ('.', 'B', '.'),
        ('B', '.', '.'),
        ('W', '.', '.')
    )

    tile_03 = (
        ('.', 'B', '.'),
        ('B', 'B', '.'),
        ('.', 'B', '.')
    )

    tile_04 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board_01b = (
        ('1 ', '2 ', '3 '),
        ('7 ', '8 ', '9 '),
        ('13', '14', '15')
    )
    board_02b = (
        ('4 ', '5 ', '6 '),
        ('10', '11', '12'),
        ('16', '17', '18')
    )

    board_03b = (
        ('19', '20', '21'),
        ('25', '26', '27'),
        ('31', '32', '33')
    )

    board_04b = (
        ('22', '23', '24'),
        ('28', '29', '30'),
        ('34', '35', '36')
    )

    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)
    board_numbered = b.Board(board_01b, board_02b, board_03b, board_04b)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("Left Diagonal Upper-band Tests:")
    utils.print_pretty_board(game.get_state())

    print()
    print("Diagonal Upper-band Tests:")
    print(f"Player1 winner: {g._is_solution_diagonal_right(game.get_state(), player1)}")
    print(f"Player2 winner: {g._is_solution_diagonal_right(game.get_state(), player2)}")
    print(utils.utility_function_linear(board.get_board_state(), player1))
    # print(utils.utility_function_linear(board.get_board_state(), player1))
    # print(utils.utility_function_linear(board.get_board_state(), player2))
    print(utils.utility_function_linear(board.get_board_state(), player2))
    print(utils.utility_function_diagonal(board.get_board_state(), player1))
    print(utils.utility_function_diagonal_right_left(board_numbered.get_board_state(), player1))
    print(utils.utility_function_diagonal(board.get_board_state(), player2))
    print( utils.utility_function_vertical(board.get_board_state(), player1))
    print(utils.utility_function_vertical(board.get_board_state(), player2))


# print("Updating board 1 with some moves")
# game.result_place_marble(game.get_state(), (1, 3))
# utils.print_pretty_board(game.get_state())
# print()
# game.result_rotate(game.get_state(), (1, 'L'))
# print("Bullshit")
# utils.print_pretty_board(game.get_state())
# print()


# state_02 = current_game.result_place_marble(state_01.get_board(), ((2, 4), (1, 'R')))
# print("More shit")
# state_02.print_pretty_board()
# print()
#
# print()
# state_03 = current_game.result_place_marble(state_02.get_board(), ((4, 2), (1, 'R')))
# print("More shit")
# state_03.print_pretty_board()
# print()
#
#
# print()
# state_04 = current_game.result_place_marble(state_03.get_board(), ((4, 1), (4, 'R')))
# print("Play 4/1 4L")
# state_04.print_pretty_board()
# print()

def get_test_board_01():
    tile_01 = (
        ('W', 'W', 'W'),
        ('W', 'B', 'W'),
        ('W', 'W', '.')
    )

    tile_02 = (
        ('W', '.', '.'),
        ('W', '.', '.'),
        ('W', 'W', 'W')
    )

    tile_03 = (
        ('W', 'B', 'W'),
        ('W', 'B', '.'),
        ('W', 'W', 'W')
    )

    tile_04 = (
        ('B', 'W', 'W'),
        ('W', 'B', 'W'),
        ('W', 'W', 'B')
    )

    return b.Board(tile_01, tile_02,
                    tile_03, tile_04)


def get_player_pieces_test():
    game = g.Problem()

    player_01 = p.Player("Carl", "W", "Human")
    player_02 = p.Player("Luke", "B", "Human")

    game.add_player(player_01)
    game.add_player(player_02)

    print()
    print(f"Player 1: {player_01}")
    print(f"Player 2: {player_02}")




    game.set_board(get_test_board_01())
    game.set_state(game.get_state())
    print()
    print("get_player_pieces_test:")
    utils.print_pretty_board(game.get_state())

    actions = g.get_actions_for_alpha_beta(game.get_state(), player_01)
    print(f"{len(actions)} action(s)")
    print("Most valuable actions listed first")
    count = 1
    for action in actions:
        print(f"{count}: {action}")
        count +=1


    print("finished test")


########################################################
#                   Main Program
########################################################


if __name__ == '__main__':

    # tile_location_test()
    # solution_horizontal_test()
    # solution_vertical_test()
    # solution_left_diagonal_center_band_test()
    # solution_left_diagonal_lower_band_test()
    # solution_left_diagonal_upper_band_test()
    # solution_right_diagonal_center_band_test()
    # solution_right_diagonal_lower_band_test()
    # solution_right_diagonal_upper_band_test()

    get_player_pieces_test()

