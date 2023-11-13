import requests
from player import Player
from playerReader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = []
        self.reader = reader
        self.player_list = []
    
    def top_scorers_by_nationality(self, nationality):
        self.players = self.reader.get_players()

        for player in self.players:
            if player.nationality == nationality:
                self.player_list.append(player)

        self.player_list.sort(key=lambda player: player.total_points(), reverse=True)
        
        return self.player_list



