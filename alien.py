import pygame
from pygame.sprite import Sprite, AbstractGroup


class Alien(Sprite):
    """Класс одного пришельца"""
    def __init__(self, ai_game, *groups: AbstractGroup):
        """Инициализация пришельца и его начальной позиции"""
        super().__init__(*groups)
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца
        self.image = pygame.image.load("images/purple_alien.png")
        self.rect = self.image.get_rect()

        # Каждый новый пришелец в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Точная горизонтальная позиция пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """True если пришелец достигает край"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещение пришельца влево или вправо"""
        self.x = (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x += self.x