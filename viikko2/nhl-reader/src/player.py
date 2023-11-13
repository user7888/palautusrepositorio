class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['assists']
        self.assists = dict['goals']
    
    def total_points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:2} {self.goals:2} + {self.assists:2} = {self.total_points()}"
