class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.game_score = "Love-All"

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
        
        self.update_game_score()
    
    def advantage_scoring(self):
        score_difference = self.player1_score - self. player2_score

        if score_difference == 1:
            self.game_score = "Advantage player1"
        elif score_difference == -1:
            self.game_score = "Advantage player2"
        elif score_difference >= 2:
            self.game_score = "Win for player1"
        else:
            self.game_score = "Win for player2"
    
    def tie_scoring(self):
        if self.player1_score == 0:
            self.game_score = "Love-All"
        elif self.player1_score == 1:
            self.game_score = "Fifteen-All"
        elif self.player1_score == 2:
            self.game_score = "Thirty-All"
        else:
            self.game_score = "Deuce"

    def update_game_score(self):
        advantage_limit = 4
        score_names = {0: "Love",
                       1: "Fifteen",
                       2: "Thirty",
                       3: "Forty"}
        
        if self.player1_score == self.player2_score:
            self.tie_scoring()
        elif self.player1_score >= advantage_limit or self.player2_score >= advantage_limit:
            self.advantage_scoring()        
        else:
            self.game_score = f"{score_names[self.player1_score]}-{score_names[self.player2_score]}"

    def get_score(self):         
        return self.game_score

