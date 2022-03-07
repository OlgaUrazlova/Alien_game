import pygame


class Ship:
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализация корабля и его начальной позиции"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Корабль отображается внизу игоровой области
        self.rect.midbottom = self.screen_rect.midbottom

        # Координата центра корабля
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновление позиции корабля с учетом флага перемещения"""
        # Обновляется атрибут x объекта ship, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основе self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Возвращаем корабль в центр"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)