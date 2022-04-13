from msilib.schema import Class
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Класс для управления пулями, выпущенными кораблем'''
    def __init__(self, ai_settings, screen, ship):
        '''Создает объект пули в текущей позиции корабля'''
        super().__init__()
        self.screen = screen

        #Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centrx
        self.rect.top = ship.rect.top

        #Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


