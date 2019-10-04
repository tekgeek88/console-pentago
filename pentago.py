import os
import game as g
import player as p
import utils
import random
import tree
from time import time
from termcolor import colored
import board

## PA2 Pentago
## Carl Argabright

# The max depth is the max depth of parent nodes to be expanded
# i.e. a serach depth of 3 will yield a 2-ply game where two moves are foreseen ahead
SEARCH_DEPTH = 3
#Uncomment your desired search method
# SEARCH_METHOD = "MiniMax"
SEARCH_METHOD = "AlphaBeta"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def parse_player(input_player):
    token = input_player.split(" ")
    if token[0].upper() == 'QUIT':
        print("Thank you for playing!")
        exit(0)
    if len(token) < 3:
        print("Not enough tokens to create player, try again!")
        return None
    else:
        name = token[0]
        color = token[1]
        player_type = token[2]
        return p.Player(name, color, player_type)


def print_past_moves(game, player_moves):
    ## Tuple indexes
    index_move = 0
    index_time = 1
    player = None
    if player_moves:
        i = 0

        for p in player_moves:
            move_tuple = p[index_move]
            time_tuple = p[index_time]
            if i % 2 == 0:
                player = game.get_player(0)
            else:
                player = game.get_player(1)
            print(f"{move_tuple[0][0]}/{move_tuple[0][1]}, {move_tuple[1][0]}{move_tuple[1][1]}, {player.get_name().ljust(player.get_padding())} - {time_tuple}")
            i+=1


def print_player_info(game_count, game):
    print(f"Player 01: {game.get_player(0).get_name()} {game.get_player(0).get_type()}")
    print(f"Player 02: {game.get_player(1).get_name()} {game.get_player(1).get_type()}")
    print(f"Player 01: {game.get_player(0).get_color()}")
    print(f"Player 02: {game.get_player(1).get_color()}")
    if game_count % 2 == 0:
        print(f"Player to move next: {1}")
    else:
        print(f"Player to move next: {2}")


def parse_move(input_move):
    move_tup = rotate_tup = None
    input_move = input_move.replace('/', ' ')
    move = input_move.split(' ')
    if len(move) != 3:
        print("Failure parsing move please retry!")
        return None, None
    try:
        # player_moves.append(input_move)
        move_tup = int(move[0]), int(move[1])
        rotate_tup = int(move[2][0]), move[2][1]
        if move_tup[0] < 1 or move_tup[0] > 4:
            print("Please select a board between 1 and 4 and try again!")
            return None, None
        elif move_tup[1] < 1 or move_tup[1] > 9:
            print("Please select a position between 1 and 9 and try again!")
            return None, None
        if rotate_tup[0] < 1 or rotate_tup[0] > 4:
            print("Please select a board to rotate between 1 and 4 and try again!")
            return None, None
        if not(rotate_tup[1] == 'L' or rotate_tup[1] == 'R'):
            print("Must rotate either Right or Left please try again!")
            return None, None

    except Exception:
        print("Invalid input please try again!")
        move_tup = rotate_tup = None

    if game.is_occupied(move_tup, game.get_state()):
        print("That board location is already taken please try again!")
        move_tup = rotate_tup = None
    return move_tup, rotate_tup


def print_player_directions():
    clear_screen()
    print()
    print("Welcome to console Pentago!")
    print()
    print("To play please enter your players info on one line separated by a space:\n")
    print("\tPlayers name: \"First\" or \"Last\"")
    print("\tPlayers color: \"B\" or \"W\"")
    print("\tPlayers type: \"AI\" or \"Human\"")
    print()
    print("Ex: Carl W Human")
    print()
    print("type \"quit\' at anytime to quit the game and return to the command line")


def print_game_play_directions():
    print("Enter Move:")
    print("    Enter moves using the following format")
    print("    {Block Number}/{Block index} {block}{direction}")
    print("    Example: 2/1 2R")


def display_game_state(game, player_moves):
    print()
    print_player_info(game.get_state_count(), game)
    utils.print_pretty_board(game.get_state())
    print_past_moves(game, player_moves)


def game_loop(game):
    algorithm = SEARCH_METHOD
    depth_limit = SEARCH_DEPTH
    has_won = False
    players_move_list = []
    game_result = ""

    game_start = time()
    while not has_won:
        count = tree.Counter()
        clear_screen()

        # Gather the players
        current_player_number = game.get_player_turn()
        current_player = game.get_player(current_player_number - 1)
        other_player_number = 1 if current_player_number == 2 else 2
        other_player = game.get_player(other_player_number - 1)

        is_current_player_max = False
        if current_player == game.get_player(0):
            is_current_player_max = True

        # Display the players stats and the game state
        display_game_state(game, players_move_list)

        # Each state must be updated per move or the game will loop infinite
        # If player is AI
        timeStart = time()
        if current_player.get_type() == 'AI':
            ai_action = None
            print(f"{current_player.get_name()} is thinking...")

            if algorithm == "MiniMax":
                if is_current_player_max:
                    ai_action = tree.minimax_decision(game.get_state(), depth_limit, current_player, other_player, True, count)
                else:
                    ai_action = tree.minimax_decision(game.get_state(), depth_limit, current_player, other_player, False, count)

            elif algorithm == "AlphaBeta":
                depth_limit = SEARCH_DEPTH
                if is_current_player_max:
                    ai_action = tree.alpha_beta_decision(game.get_state(), depth_limit, current_player, other_player, True, count)
                else:
                    ai_action = tree.alpha_beta_decision(game.get_state(), depth_limit, other_player, current_player, False, count)

            timeStop = time()
            elapsedTime = timeStop - timeStart
            hours, rem = divmod(elapsedTime, 3600)
            minutes, seconds = divmod(rem, 60)
            time_taken = f"{int(minutes):0>2}:{seconds:05.2f}"
            # Add the AI move to the board
            players_move_list.append((ai_action, time_taken))

            # Drop the marble for the given move action
            temp_state = g.result_place_marble(game.get_state(), current_player, ai_action[0])

            # If the marble drop causes a win
            if (g.is_winner(temp_state, current_player)):
                game.set_state(temp_state)
                game_result = f"Player {current_player_number}: {current_player.get_name()} {current_player.get_type()}: has won!"
                has_won = True

            # Rotate board
            else:
                game.set_state(g.result_rotate(temp_state, ai_action[1]))
                game.increment_state_count()

                # If the rotate caused the current player to win
                if g.is_winner(game.get_state(), current_player):
                    # And if the other player has won
                    if g.is_winner(game.get_state(), other_player):
                        game_result = "The game has been declared a TIE!"
                        has_won = True
                    else:
                        game_result = f"Player {current_player_number}: {current_player.get_name()} {current_player.get_type()}: has won!"
                        has_won = True

                # If the rotate caused the other player to win
                elif g.is_winner(game.get_state(), other_player):
                    game_result = f"Player {other_player_number}: {other_player.get_name()} {other_player.get_type()}: has won!"
                    has_won = True

                # If the last move and rotate is not a win
                elif game.get_state_count() == 36:
                    game_result = "Game is a draw all moves have been taken"
                    has_won = True

        # If player is Human
        elif current_player.get_type() == 'HUMAN':
            print_game_play_directions()
            input_move = input("> ").upper()
            if input_move == 'QUIT':
                print("Thank you for playing!")
                exit(0)
            else:
                # Parse Move
                move_tup = rotate_tup = None
                while not move_tup and not rotate_tup:
                    move_tup, rotate_tup = parse_move(input_move)
                    if not move_tup and not rotate_tup:
                        input_move = input("> ").upper()
                        if input_move == 'QUIT':
                            print("Thank you for playing!")
                            exit(0)

                timeStop = time()
                elapsedTime = timeStop - timeStart
                hours, rem = divmod(elapsedTime, 3600)
                minutes, seconds = divmod(rem, 60)
                time_taken = f"{int(minutes):0>2}:{seconds:05.2f}"
                # Add the AI move to the board
                # If valid move then
                players_move_list.append(((move_tup, rotate_tup), time_taken))

                # Human player places marble
                temp_state = g.result_place_marble(game.get_state(), current_player, move_tup)

                # If the marble drop causes a win
                if (g.is_winner(temp_state, current_player)):
                    game.set_state(temp_state)
                    game_result = f"Player {current_player_number}: {current_player.get_name()} {current_player.get_type()}: has won!"
                    has_won = True

                # Rotate board
                else:
                    game.set_state(g.result_rotate(temp_state, rotate_tup))
                    game.increment_state_count()
                    # If the rotate caused the current player to win
                    if g.is_winner(game.get_state(), current_player):
                        # And if the other player has won
                        if g.is_winner(game.get_state(), other_player):
                            game_result = "The game has been declared a TIE!"
                            has_won = True
                        else:
                            game_result = f"Player {current_player_number}: has won!"
                            has_won = True
                    elif g.is_winner(game.get_state(), other_player):
                        game_result = f"Player {other_player_number}: has won!"
                        has_won = True
                    # If the last move and rotate is not a win
                    elif game.get_state_count() == 36:
                        game_result = "Game is a draw all moves have been taken"
                        has_won = True

        # If player type is invalid
        else:
            print("Unsupported player type!")
            exit(1)


    game_stop = time()
    elapsedTime = game_stop - game_start
    hours, rem = divmod(elapsedTime, 3600)
    minutes, seconds = divmod(rem, 60)
    time_taken = f"{int(minutes):0>2}:{seconds:05.2f}"

    # Display the final state of the game in all cases
    display_game_state(game, players_move_list)
    print(game_result)
    print(f"Total Game time: {time_taken}")

########################################################
#                   Main Program
########################################################


if __name__ == '__main__':
    # clear_screen()
    print_player_directions()

    # Create Players
    player_01 = None
    player_02 = None

    while player_01 is None:
        input_player_01 = input("Player 1:\n>")
        player_01 = parse_player(input_player_01)

    while player_02 is None:
        input_player_02 = input("Player 2:\n>")
        player_02 = parse_player(input_player_02)

    # Set a static padding value
    p.Player.padding = max(len(player_01.get_name()), len(player_02.get_name()))

    # Create gamBe board
    game = g.Problem()
    player_list = list()
    player_list.append(player_01)
    player_list.append(player_02)


    game.add_player(player_list.pop(random.randint(0, 0)))
    game.add_player(player_list.pop())

    print(f"{game.get_player(0).get_name()} {game.get_player(0).get_type()} was randomly selected to go first")
    print()
    game_loop(game)

