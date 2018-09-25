class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #SHIP SETTING
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        #Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
    
        #Alien settings
        self.alien_speed_factor = 0.25
        self.fleet_drop_speed = 10
        
        #fleet_direciton +1 right -1 left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.25

        #fleet_direciton +1 right -1 left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
