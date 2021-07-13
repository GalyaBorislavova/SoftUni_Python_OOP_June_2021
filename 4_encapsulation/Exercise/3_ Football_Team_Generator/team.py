from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_player(self, player: Player):
        for pl in self.__players:
            if pl._Player__name == player._Player__name:
                return f"Player {pl._Player__name} has already joined"
        self.__players.append(player)
        return f"Player {player._Player__name} joined team {self._Team__name}"

    def remove_player(self, player_name: str):
        for pl in self.__players:
            if player_name == pl._Player__name:
                self.__players.remove(pl)
                return pl
        return f"Player {player_name} not found"


# if __name__ == "__main__":
#     p = Player("Pall", 1, 3, 5, 7)
#
#     print("Player name:", p.name)
#     print("Points sprint:", p._Player__sprint)
#     print("Points dribble:", p._Player__dribble)
#     print("Points passing:", p._Player__passing)
#     print("Points shooting:", p._Player__shooting)
#
#     print("\ncalling the __str__ method")
#     print(p)
#
#     print("\nAbout the team")
#     t = Team("Best", 10)
#     print("Team name:", t._Team__name)
#     print("Teams points:", t._Team__rating)
#     print("Teams players:", len(t._Team__players))
#     print(t.add_player(p))
#     print(t.add_player(p))
#     print("Teams players:", len(t._Team__players))
#     print(t.remove_player("Pall"))
#     print(t.remove_player("Pall"))
