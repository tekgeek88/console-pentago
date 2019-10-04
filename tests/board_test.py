import board
import game
import utils


board_01 = (
    ('W', '.', '.'),
    ('W', '.', '.'),
    ('W', '.', '.')
)

board_02 = (
    ('.', 'W', '.'),
    ('.', 'W', '.'),
    ('.', 'W', '.')
)

board_03 = (
    ('B', 'B', 'B'),
    ('.', '.', '.'),
    ('.', '.', '.')
)

board_04 = (
    ('B', '.', '.'),
    ('.', 'B', '.'),
    ('.', '.', 'B')
)


print("Creating a test_board with default values...")
test_board = board.Board()
utils.print_pretty_board(test_board.get_board_state())
print()


print("Modifying board 1")
test_board_01 = board.Board(board_01, test_board.get_tile(2), )
utils.print_pretty_board(test_board_01.get_board_state())
print()


print("Modifying board 2")
test_board_02 = board.Board(test_board_01.get_tile(1), board_02)
utils.print_pretty_board(test_board_02.get_board_state())
print()


print("Modifying board 3")
test_board_03 = board.Board(test_board_02.get_tile(1), test_board_02.get_tile(2), board_03)
utils.print_pretty_board(test_board_03.get_board_state())
print()


print("Modifying board 4")
test_board_04 = board.Board(test_board_03.get_tile(1), test_board_03.get_tile(2), test_board_03.get_tile(3), board_04)
utils.print_pretty_board(test_board_04.get_board_state())
print()


print("Rotating test board 04: 1R")
pre_rotate = test_board_04.get_tile(1)
after_rotate = test_board_04.rotate_tile_right(test_board_04.get_tile(1))

test_board_04_rotated_r = board.Board(after_rotate,
                                      test_board_04.get_tile(2),
                                      test_board_04.get_tile(3),
                                      test_board_04.get_tile(4))
# test_board_04_rotated_r.print_pretty_board()
print()

