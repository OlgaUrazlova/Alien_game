import pygame
from pygame.sprite import Sprite, AbstractGroup


class Alien(Sprite):
    """Класс одного пришельца"""
    def __init__(self, ai_game, *groups: AbstractGroup):
        """Инициализация пришельца и его начальной позиции"""
        super().__init__(*groups)
        self.screen = ai_game.screen

        # Загрузка изображения пришельца
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Каждый новый пришелец в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Точная горизонтальная позиция пришельца
        self.x = float(self.rect.x)