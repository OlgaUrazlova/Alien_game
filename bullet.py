import pygame
from pygame.sprite import Sprite, AbstractGroup


class Bullet(Sprite):
    """Класс для управления снарядами"""

    def __init__(self, ai_game, *groups: AbstractGroup):
        """Создать снаряды в текущей позиции корабля"""
        super().__init__(*groups)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0,0) и назначение верной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном виде
        self.y = float(self.rect.y)

    def update(self):
        """Переместить снаряд вверх экрана"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
