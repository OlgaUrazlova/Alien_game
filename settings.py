class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Настройки снарядов
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 вправо, -1 влево