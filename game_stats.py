class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False
        self.high_score = self.read_high_score()
        self.level = 1
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0

    def read_high_score(self):
        f = open('highscore.txt', 'r')
        str_score = f.readline()
        f.close()
        return int(str_score)
        
