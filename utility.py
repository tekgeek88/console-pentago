import utils
import player as p


def utility_in_line(pay_line, player: p.Player, is_max):
    # The amount of utility for 0, 2, 3, 4 elements in a row
    scores = [0, 10, 25, 1000, 2000]
    current_utility = 0
    previous_piece = current_piece = None
    count = i = 0
    for i in range(1, len(pay_line)):
        previous_piece, current_piece = pay_line[i - 1], pay_line[i]
        if previous_piece != player.get_color() and previous_piece != '.'\
                or current_piece != player.get_color() and current_piece != '.':
            current_utility = 0
            count = 0
            break
        # Count the number of things in the current line that are repeating
        if previous_piece == current_piece:
            count += 1
        else:
            # If the pieces are the current players pieces we add utility
            if previous_piece == player.get_color():
                if not count:
                    current_utility += 1
                current_utility += scores[count]
            count = 0
    # Handle the case where the last two elements are equal
    if count:
        if previous_piece != player.get_color() and previous_piece != '.':
            current_utility = 0
        elif previous_piece == player.get_color():
            current_utility += scores[count]
    else:
        if previous_piece != player.get_color() and previous_piece != '.':
            current_utility = 0
        elif current_piece == player.get_color() and previous_piece != player.get_color():
            current_utility += 1
    if current_utility == 20:
        current_utility = 250
    elif current_utility == 3:
        current_utility = 75
    if current_utility == 26:
        current_utility = 250
    if current_utility == 11:
        current_utility = 75
    return current_utility


def utility_total_in_lines(pay_lines, player: p.Player, is_max):
    total_utility = 0
    for line in pay_lines:
        total_utility += utility_in_line(line, player, is_max)
    return total_utility


def utility_in_lines(pay_lines, player: p.Player, is_max):
    utility_current = utility_max = 0
    for line in pay_lines:
        utility_current = utility_in_line(line, player, is_max)
        utility_max = max(utility_max, utility_current)
    return utility_max


def _get_lines_horizontal_left(state):
    #Left Side
    lines = []
    for y in range(6):
        current_line = []
        for x in range(5):
            board, row, column = utils.get_board_row_column((x, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
        lines.append(current_line)
    return lines


def _get_lines_horizontal_right(state):
    # Right Side
    lines = []
    for y in range(6):
        current_line = []
        for x in range(1, 6):
            board, row, column = utils.get_board_row_column((x, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
        lines.append(current_line)
    return lines


def _get_lines_vertical_top(state):
    lines = []
    for x in range(6):
        current_line = []
        for y in range(5):
            board, row, column = utils.get_board_row_column((x, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
        lines.append(current_line)
    return lines


def _get_lines_vertical_bottom(state):
    lines = []
    for x in range(6):
        current_line = []
        for y in range(1, 6):
            board, row, column = utils.get_board_row_column((x, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
        lines.append(current_line)
    return lines


def _get_lines_diagonal_left_upperband(state):
    lines = []
    current_line = []
    for y in range(0,5):
        board, row, column = utils.get_board_row_column((y+1, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _get_lines_diagonal_left_lowerband(state):
    lines = []
    current_line = []
    for y in range(1, 6):
        board, row, column = utils.get_board_row_column((y-1, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _get_lines_diagonal_left_centerband_upper(state):
    # Center band from top left
    lines = []
    current_line = []
    for y in range(5):
        board, row, column = utils.get_board_row_column((y, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines

def _get_lines_diagonal_left_centerband_lower(state):
    # Center band from bottom right
    lines = []
    current_line = []
    for y in range(5, 0, -1):
            board, row, column = utils.get_board_row_column((y, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _get_lines_diagonal_right_upperband(state):
    lines = []
    current_line = []
    for y in range(0,5):
        board, row, column = utils.get_board_row_column((4-y, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _get_lines_diagonal_right_lowerband(state):
    lines = []
    current_line = []
    for y in range(1, 6):
        board, row, column = utils.get_board_row_column((6-y, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _get_lines_diagonal_right_centerband_upper(state):
    # Center band from top left
    lines = []
    current_line = []
    for y in range(0, 5):
        board, row, column = utils.get_board_row_column((5-y, y))
        current_piece = state[board][row][column]
        current_line.append(current_piece)
    lines.append(current_line)
    return lines
#
def _get_lines_diagonal_right_centerband_lower(state):
    # Center band from bottom left
    lines = []
    current_line = []
    for y in range(5, 0, -1):
            board, row, column = utils.get_board_row_column((5-y, y))
            current_piece = state[board][row][column]
            current_line.append(current_piece)
    lines.append(current_line)
    return lines


def _utility_horizontal(state, player, is_max):
    hori_left_utility = utility_in_lines(_get_lines_horizontal_left(state), player, is_max)
    hori_right_utility = utility_in_lines(_get_lines_horizontal_right(state), player, is_max)
    utility_val = max(hori_left_utility, hori_right_utility)
    return utility_val


def _utility_vertical(state, player, is_max):
    verti_bottom_utility = utility_in_lines(_get_lines_vertical_bottom(state), player, is_max)
    verti_top_utility = utility_in_lines(_get_lines_vertical_top(state), player, is_max)
    utility_val = 0
    return max(verti_bottom_utility, verti_top_utility)


def _utility_diagonal_left(state, player, is_max):
    diag_left_upper = utility_in_lines(_get_lines_diagonal_left_upperband(state), player, is_max)
    diag_left_lower = utility_in_lines(_get_lines_diagonal_left_lowerband(state), player, is_max)
    diag_center_upper = utility_in_lines(_get_lines_diagonal_left_centerband_upper(state), player, is_max)
    diag_center_lower = utility_in_lines(_get_lines_diagonal_left_centerband_lower(state), player, is_max)
    utility_val = max(max(max(diag_left_upper, diag_left_lower), diag_center_upper), diag_center_lower)
    return utility_val


def _utility_diagonal_right(state, player, is_max):
    diag_right_upper = utility_in_lines(_get_lines_diagonal_right_upperband(state), player, is_max)
    diag_right_lower = utility_in_lines(_get_lines_diagonal_right_lowerband(state), player, is_max)
    diag_right_center_upper = utility_in_lines(_get_lines_diagonal_right_centerband_upper(state), player, is_max)
    diag_right_center_lower = utility_in_lines(_get_lines_diagonal_right_centerband_lower(state), player, is_max)
    utility_val = max(max(max(diag_right_upper, diag_right_lower), diag_right_center_upper), diag_right_center_lower)
    return utility_val



def utility(state, player, is_max):
    hori_utility = _utility_horizontal(state, player, is_max)
    veri_utility = _utility_vertical(state, player, is_max)
    diag_left_utility = _utility_diagonal_left(state, player, is_max)
    diag_right_utility = _utility_diagonal_right(state, player, is_max)
    utility_val = max(max(max(hori_utility, veri_utility), diag_left_utility), diag_right_utility)
    if not is_max:
        utility_val *= -1
    return utility_val