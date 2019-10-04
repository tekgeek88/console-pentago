import player as p
import utils
import game as g
import board as b


def player_creation_test():
    default_player = p.Player()
    print("Default player:")
    print(default_player)
    print()
    # With named parameters
    print("Player: Carl:")
    player_carl = p.Player(player_name="Carl", player_color="W", player_type="Human")
    print(player_carl)
    print()
    # jsut a basic constructor
    print("Player: Carl_02:")
    player_carl_02 = p.Player("Carl", "w", "human")
    print(player_carl_02)
    print()
    print("Player: AI 01")
    player_ai_01 = p.Player("AI 01", "B", "ai")
    print(player_ai_01)
    print()


if __name__ == '__main__':

    player_creation_test()