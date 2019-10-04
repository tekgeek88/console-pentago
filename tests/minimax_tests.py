import tree
import game as g
import player as p
import utils
import board as b
import utility as u

game = g.Problem()

player_01 = p.Player("Carl", "W", "Human")
player_02 = p.Player("Luke", "B", "Human")

game.add_player(player_01)
game.add_player(player_02)

print()
print(f"Player 1: {player_01}")
print(f"Player 2: {player_02}")


def ai_action_test():
    # Horizontal
    tile_01 = (
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', 'W', '.')
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
        ('.', '.', '.'),
        ('.', '.', '.'),
        ('.', '.', '.')
    )
    board = b.Board(tile_01, tile_02,
                    tile_03, tile_04)

    game.set_board(board)
    game.set_state(board.get_board_state())
    print()
    print("AI Action Test:")
    utils.print_pretty_board(game.get_state())

    depth_limit = 0
    is_max = None
    is_swapped = False
    if is_swapped:
        current_player = player_02
        other_player = player_01
        is_max = False
    else:
        current_player = player_01
        other_player = player_02
        is_max = True

    print(f"Utility from utils: {u.utility(game.get_state(), current_player, is_max)}")
    print()
    depth = 3
    ai_action = tree.minimax_decision(game.get_state(), depth, current_player, other_player, True)
    print(f"Action determined for {current_player.get_name()}: {ai_action}")
    game.set_state(g.result(game.get_state(), current_player, ai_action))

    print("Final board after action taken:")
    utils.print_pretty_board(game.get_state())


########################################################
#                   Main Program
########################################################


if __name__ == '__main__':

    ai_action_test()
