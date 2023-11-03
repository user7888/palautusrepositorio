import unittest
from statistics_service import StatisticsService
from player import Player

class StubPlayerReader:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            StubPlayerReader()
        )

    def test_search(self):
        player_search = self.stats.search("Kurri")
        self.assertEqual(player_search.name, "Kurri")
        self.assertEqual(player_search.team, "EDM")
        # Search returns None if player does not exist
        player_search = self.stats.search("Non")
        self.assertEqual(player_search, None)
    
    def test_team_function_returns_all_players_in_team(self):
        players_in_team = self.stats.team("EDM")
        self.assertEqual(len(players_in_team), 3)
    
    def test_top_function_returns_top_n_plus_one_players(self):
        top_n = self.stats.top(2)
        self.assertEqual(len(top_n), 3)

    def test_top_function_returns_sorted_by_points(self):
        top_n = self.stats.top(2)
        # Search max from player list sorted by points
        self.assertEqual(top_n[0].points, max(self.stats._players, key=lambda player: player.points).points)  

    def test_top_function_returns_sorted_by_goals(self):
        top_n = self.stats.top(2, 2)
        # Search max from player list sorted by goals
        self.assertEqual(top_n[0].goals, max(self.stats._players, key=lambda player: player.goals).goals) 

    def test_top_function_returns_sorted_by_assists(self):
        top_n = self.stats.top(2, 3)
        # Search max from player list sorted by assists
        self.assertEqual(top_n[0].assists, max(self.stats._players, key=lambda player: player.assists).assists) 



