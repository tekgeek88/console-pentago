class Player:

    padding = 0

    def __init__(self, player_name="players_name", player_color="players_color", player_type="player_type"):

        self._name = player_name
        self._color = player_color.upper()
        self._type = player_type.upper()

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_padding(self):
        return Player.padding

    def get_type(self):
        return self._type

    def __str__(self):
        return f"Name: {self._name}, Color: {self._color}, Type: {self._type}"