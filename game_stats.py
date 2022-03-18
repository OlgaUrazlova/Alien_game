class GameStats:
    """Отслеживание статистики"""
    def __init__(self, ai_game):
        """Инициализация"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Статистика, меняющаяся в ходе игры"""
        ships_left = self.settings.ship_limit


