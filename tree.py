import game as g
import sys
import player as p
import utility as u


infinity_neg = (sys.maxsize - 1) * -1
infinity_pos = sys.maxsize


class Counter:

    count = 0

    def increment_count(self):
        self.count += 1

    def get_count(self):
        return self.count


def minimax_decision(state, depth, player_max: p.Player, player_min: p.Player, is_max, count: Counter):
    transition_states = set()
    count.increment_count()
    move_count = 0
    best_move = None
    moves = g.get_actions(state)
    if is_max:
        best_score = infinity_neg
        for move in moves:
            clone = g.result(state, player_max, move)
            if clone not in transition_states:
                move_count += 1
                transition_states.add(clone)
                if depth - 1 > 0:
                    count.increment_count()
                score = min_value(clone, depth - 1, player_max, player_min, transition_states, count)
                if score > best_score:
                    best_score = score
                    best_move = move
    else:
        best_score = infinity_pos
        for move in moves:
            clone = g.result(state, player_min, move)
            if clone not in transition_states:
                move_count += 1
                transition_states.add(clone)
                if depth - 1 > 0:
                    count.increment_count()
                score = max_value(clone, depth - 1, player_max, player_min, transition_states, count)
                if score < best_score:
                    best_score = score
                    best_move = move
    print(f"Number Expanded: {count.get_count()}")
    return best_move


def min_value(state, depth, player_max, player_min, transition_states, count: Counter):
    # Base case
    if g.is_winner(state, player_max) or depth == 0:
        value = u.utility(state, player_max, True)
        return value
    moves = g.get_actions(state)
    best_score = sys.maxsize
    for move in moves:
        clone = g.result(state, player_min, move)
        if clone not in transition_states:
            if depth - 1 > 0:
                count.increment_count()
            score = max_value(clone, depth - 1, player_max, player_min, transition_states, count)
            if score < best_score:
                best_score = score
    return best_score


def max_value(state, depth, player_max, player_min, transition_states, count: Counter):
    # Base case
    if g.is_winner(state, player_min) or depth == 0:
        value = u.utility(state, player_min, False)
        return value
    moves = g.get_actions(state)
    best_score = infinity_neg
    for move in moves:
        score = None
        clone = g.result(state, player_max, move)
        if clone not in transition_states:
            if depth - 1> 0:
                count.increment_count()
            score = min_value(clone, depth - 1, player_max, player_min, transition_states, count)
            if score > best_score:
                best_score = score
    return best_score


def alpha_beta_decision(state, depth, player_max: p.Player, player_min: p.Player, is_max, count: Counter):
    is_max = True
    transition_states = set()
    number_expanded = count.increment_count()
    move_count = 0
    alpha = infinity_neg
    beta = infinity_pos
    best_move = None
    if is_max:
        moves = g.get_actions_for_alpha_beta(state, player_max)
        best_score = infinity_neg
        for move in moves:
            clone = g.result(state, player_max, move)
            if clone not in transition_states:
                move_count += 1
                transition_states.add(clone)
                if depth - 1 > 0:
                    count.increment_count()
                score = min_value_alpha_beta(clone, depth - 1, player_max, player_min, alpha, beta, transition_states, count)
                if score > alpha:
                    alpha = score
                    best_move = move
    else:
        moves = g.get_actions_for_alpha_beta(state, player_min)
        for move in moves:
            clone = g.result(state, player_min, move)
            if clone not in transition_states:
                move_count += 1
                transition_states.add(clone)
                if depth - 1 > 0:
                    number_expanded += 1
                score = max_value_alpha_beta(clone, depth - 1, player_max, player_min, alpha, beta, transition_states, count)
                if score < beta:
                    alpha = score
                    best_move = move
    print(f"Number Expanded: {count.get_count()}")
    return best_move


def min_value_alpha_beta(state, depth, player_max, player_min, alpha, beta, transition_states, count: Counter):
    # Base case
    if g.is_winner(state, player_max) or depth == 0:
        best_score = u.utility(state, player_max, True)
        return best_score
    moves = g.get_actions_for_alpha_beta(state, player_min)
    best_score = infinity_pos
    for move in moves:
        clone = g.result(state, player_min, move)
        if clone not in transition_states:
            if depth - 1 > 0:
                count.increment_count()
            child_value = max_value_alpha_beta(clone, depth - 1, player_max, player_min, alpha, beta, transition_states, count)
            best_score = min(best_score, child_value)
            if best_score <= alpha:
                return best_score
            beta = min(beta, best_score)
    return best_score


def max_value_alpha_beta(state, depth, player_max, player_min, alpha, beta, transition_states, count: Counter):
    # Base case
    if g.is_winner(state, player_min) or depth == 0:
        best_score = u.utility(state, player_min, False)
        return best_score
    moves = g.get_actions_for_alpha_beta(state, player_max)
    best_score = infinity_neg
    for move in moves:
        clone = g.result(state, player_max, move)
        if clone not in transition_states:
            if depth -1 > 0:
                count.increment_count()
            score = min_value_alpha_beta(clone, depth - 1, player_max, player_min, alpha, beta, transition_states, count)
            best_score = max(best_score, score)
            if best_score >= beta:
                return best_score
            alpha = max(alpha, best_score)
    return best_score
