class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
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
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direciton +1 right -1 left
        self.fleet_direction = 1
