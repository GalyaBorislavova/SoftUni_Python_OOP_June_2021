from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, current_player: Player):
        if current_player.guild == "Unaffiliated":
            current_player.guild = self.name
            self.players.append(current_player)
            return f"Welcome player {current_player.name} to the guild {self.name}"
        elif current_player.guild == self.name:
            return f"Player {current_player.name} is already in the guild."
        return f"Player {current_player.name} is in another guild."

    def kick_player(self, player_name: str):
        for pl in self.players:
            if pl.name == player_name:
                pl.guild = "Unaffiliated"
                return f"Player {pl.name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = [Player.player_info(p) for p in self.players]
        return f"Guild: {self.name}" + "\n" + "\n".join(players_info)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
