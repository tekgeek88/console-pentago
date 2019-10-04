from board import Board
import utils
import player as p
from typing import List
import random


class Problem:

    def __init__(self):
        self._board = Board()
        self._players: List[p.Player] = list()
        self._INITIAL_STATE = self._board.get_board_state()
        self._state = self._INITIAL_STATE
        self._state_count = 0

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def get_player_turn(self):
        """ Defines which player has the move in a state. """
        return 1 if self._state_count % 2 == 0 else 2

    def get_state_count(self):
        return self._state_count

    def set_state_count(self, number_of_states):
        self._state_count = number_of_states

    def increment_state_count(self):
        self._state_count += 1

    def is_occupied(self, move_tuple, state):
        x, y = utils.get_2d_point(move_tuple[1])
        is_occupied = state[move_tuple[0] - 1][y][x] != '.'
        return is_occupied

    def add_player(self, player):
        self._players.append(player)

    def get_player(self, index) -> p.Player:
        return self._players[index]


def _is_solution_horizontal(state, player: p.Player):
    is_solution = False
    for left_tile in range(0, 3, 2):
        for row in range(3):
            i = 2
            j = 0
            while i >= 0 and j <= 2:
                # Base Case
                if i == 0 and j == 2:
                    if state[left_tile][row][i] == player.get_color() or state[left_tile + 1][row][
                        j] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[left_tile][row][i] != player.get_color() or state[left_tile + 1][row][
                    j] != player.get_color():
                    break
                i -= 1
                j += 1
    return is_solution


def _is_solution_vertical(state, player: p.Player):
    is_solution = False
    for top_tile in range(0, 2):
        for column in range(3):
            i = 2
            j = 0
            while i >= 0 and j <= 2:
                # Base Case
                if i == 0 and j == 2:
                    if state[top_tile][i][column] == player.get_color() or state[top_tile + 2][j][
                        column] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[top_tile][i][column] != player.get_color() or state[top_tile + 2][j][
                    column] != player.get_color():
                    break
                i -= 1
                j += 1
    return is_solution


def _is_solution_diagonal_left(state, player: p.Player):
    is_solution = False

    # Lower band
    top_tile = 0
    if state[2][0][2] == player.get_color():
        for column in range(2):
            i = 1
            while i <= 2:
                # Base case
                if i == 2:
                    if state[top_tile][i][i - 1] == player.get_color() and state[top_tile + 3][i][
                        i - 1] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[top_tile][i][i - 1] != player.get_color() or state[top_tile + 3][i][
                    i - 1] != player.get_color():
                    break
                i += 1
    # Upper Band
    top_tile = 0
    if state[1][2][0] == player.get_color():
        for column in range(2):
            i = 1
            while i <= 2:
                # Base case
                if i == 2:
                    if state[top_tile][i - 1][i] == player.get_color() and state[top_tile + 3][i - 1][
                        i] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[top_tile][i - 1][i] != player.get_color() or state[top_tile + 3][i - 1][
                    i] != player.get_color():
                    break
                i += 1

    # Middle Band
    top_tile = 0
    i = 2
    j = 2 - i
    while i >= 0 and j <= 2:
        # Base Case
        if i == 0 and j == 2:
            if state[top_tile][i][i] == player.get_color() or state[top_tile + 3][j][j] == player.get_color():
                is_solution = True
        if state[top_tile][i][i] != player.get_color() or state[top_tile + 3][j][j] != player.get_color():
            break
        i -= 1
        j = 2 - i
    return is_solution


def _is_solution_diagonal_right(state, player: p.Player):
    is_solution = False

    # Lower band
    top_tile = 1
    if state[3][0][0] == player.get_color():
        for column in range(2):
            i = 1
            j = 2
            while i <= 2:
                # Base case
                if i == 2:
                    if state[top_tile][i][j] == player.get_color() and state[top_tile + 1][i][j] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[top_tile][i][j] != player.get_color() or state[top_tile + 1][i][j] != player.get_color():
                    break
                i += 1
                j -= 1

    # Upper Band
    top_tile = 1
    if state[0][2][2] == player.get_color():
        for column in range(2):
            i = 0
            j = 1
            while i <= 1:
                # Base case
                if i == 1:
                    if state[top_tile][i][j] == player.get_color() \
                            and state[top_tile + 1][i][j] == player.get_color():
                        is_solution = True
                        return is_solution
                if state[top_tile][i][j] != player.get_color() or state[top_tile + 1][i][j] != player.get_color():
                    break
                i += 1
                j -= 1

    # Middle Band
    top_tile = 1
    i = 2
    j = 0
    while i >= 0 and j <= 2:
        # Base Case
        if i == 0 and j == 2:
            if state[top_tile][i][j] == player.get_color() or state[top_tile + 1][j][i] == player.get_color():
                is_solution = True
        if state[top_tile][i][j] != player.get_color() or state[top_tile + 1][j][i] != player.get_color():
            break
        i -= 1
        j += 1
    return is_solution


def is_winner(state, player: p.Player):
    if _is_solution_vertical(state, player):
        return True
    if _is_solution_horizontal(state, player):
        return True
    if _is_solution_diagonal_left(state, player):
        return True
    if _is_solution_diagonal_right(state, player):
        return True
    return False


def get_actions(state):
    """ Returns the set of legal moves in a state. """
    move_list = list()
    for i in range(3, -1, -1):
        for row in range(2, -1, -1):
            for column in range(2, -1, -1):
                    if state[i][row][column] == '.':
                        for board in range(1, 5, 1):
                            move_list.append((((i + 1), (column + (row * 3) + 1)), (board, 'R')))
                            move_list.append((((i+1), (column + (row * 3) + 1)), (board, 'L')))
    return move_list

def get_actions_for_alpha_beta(state, player: p.Player):
    """ Returns the set of legal moves in a state. """
    move_list = list()
    for y in range(6):
        for x in range(6):
            board, row, column = utils.get_board_row_column((x, y))
            current_piece = state[board][row][column]
            # If the current piece is open it will be a move we can make
            if current_piece == '.':
                for i in range(4):
                    # Prepare the move and rotate tuples for inisertion
                    move_tuple = (board + 1, (column + (row * 3) + 1))
                    rotate_R_tuple, rotate_L_tuple = (i+1, 'R'), (i+1, 'L')
                    # If we find an empty spot we can move to and it has one of our
                    # pieces adjacent insert it at the front of the list and break.
                    is_neighbor = False
                    for neighbor in utils.get_neighbors(x, y):
                        neighbors_piece = state[neighbor[0]][neighbor[1]][neighbor[2]]
                        if neighbors_piece == player.get_color():
                            is_neighbor = True
                    if is_neighbor:
                        move_list.insert(0, (move_tuple, rotate_R_tuple))
                        move_list.insert(0, (move_tuple, rotate_L_tuple))
                        break
                    else:
                        move_list.append((move_tuple, rotate_R_tuple))
                        move_list.append((move_tuple, rotate_L_tuple))
    return move_list

def get_players_pieces(state, player):
    """
    Returns a list of tuples representing the given players
    current pieces on the board.
    """
    piece_list = list()
    for i in range(4):
        for row in range(3):
            for column in range(3):
                    # if self.state[i][row][column] == self.get_player(self.get_player_turn()-1)[1]:
                    if state[i][row][column] == player.get_color():
                        piece_list.append(((i+1), (column + (row * 3)+1)))
    return piece_list

def result_place_marble(parent_state, player, action):
    """ The transition model, which defines the result of a move. """

    # This is needed for placing a marble
    board_num, position = action
    x, y = utils.get_2d_point(position)

    new_state = tuple()
    players_color = player.get_color()

    if board_num == 1:
        board_01 = utils.convert_2d_tuple_to_2d_array(parent_state[0])
        board_01[y][x] = players_color
        new_state = Board(utils.convert_2d_array_to_2d_tuple(board_01),
                          parent_state[1],
                          parent_state[2],
                          parent_state[3])
    elif board_num == 2:
        board_02 = utils.convert_2d_tuple_to_2d_array(parent_state[1])
        board_02[y][x] = players_color
        new_state = Board(parent_state[0],
                          utils.convert_2d_array_to_2d_tuple(board_02),
                          parent_state[2],
                          parent_state[3])
    elif board_num == 3:
        board_03 = utils.convert_2d_tuple_to_2d_array(parent_state[2])
        board_03[y][x] = players_color
        new_state = Board(parent_state[0],
                          parent_state[1],
                          utils.convert_2d_array_to_2d_tuple(board_03),
                          parent_state[3])
    elif board_num == 4:
        board_04 = utils.convert_2d_tuple_to_2d_array(parent_state[3])
        board_04[y][x] = players_color
        new_state = Board(parent_state[0],
                          parent_state[1],
                          parent_state[2],
                          utils.convert_2d_array_to_2d_tuple(board_04))
    return new_state.get_board_state()


def result_rotate(parent_state, action):
    board_num, direction = action
    new_state = tuple()
    rotated_board = tuple()
    if board_num == 1:
        if direction == 'L':
            board_1 = utils.convert_2d_tuple_to_2d_array(parent_state[0])
            rotated_board = Board.rotate_tile_left(board_1)
        elif direction == 'R':
            board_1 = utils.convert_2d_tuple_to_2d_array(parent_state[0])
            rotated_board = Board.rotate_tile_right(board_1)

        new_state = Board(rotated_board,
                          parent_state[1],
                          parent_state[2],
                          parent_state[3])
    elif board_num == 2:
        if direction == 'L':
            board_2 = utils.convert_2d_tuple_to_2d_array(parent_state[1])
            rotated_board = Board.rotate_tile_left(board_2)
        elif direction == 'R':
            board_2 = utils.convert_2d_tuple_to_2d_array(parent_state[1])
            rotated_board = Board.rotate_tile_right(board_2)

        new_state = Board(parent_state[0],
                          rotated_board,
                          parent_state[2],
                          parent_state[3])

    elif board_num == 3:
        if direction == 'L':
            board_3 = utils.convert_2d_tuple_to_2d_array(parent_state[2])
            rotated_board = Board.rotate_tile_left(board_3)
        elif direction == 'R':
            board_3 = utils.convert_2d_tuple_to_2d_array(parent_state[2])
            rotated_board = Board.rotate_tile_right(board_3)

        new_state = Board(parent_state[0],
                          parent_state[1],
                          rotated_board,
                          parent_state[3])
    elif board_num == 4:
        if direction == 'L':
            board_3 = utils.convert_2d_tuple_to_2d_array(parent_state[3])
            rotated_board = Board.rotate_tile_left(board_3)
        elif direction == 'R':
            board_3 = utils.convert_2d_tuple_to_2d_array(parent_state[3])
            rotated_board = Board.rotate_tile_right(board_3)

        new_state = Board(parent_state[0],
                          parent_state[1],
                          parent_state[2],
                          rotated_board)

    return new_state.get_board_state()

def result(parent_state, player, action):
    return result_rotate(result_place_marble(parent_state, player, action[0]), action[1])