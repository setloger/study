import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf 


def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien game')

    #Создание корабля, группы для хранения пуль, группы пришельцев
    ship = Ship(ai_settings, screen)    
    bullets = Group()
    aliens = Group()

    #Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, aliens) 

    #Назначение цвета фона
    bgcolor = (230, 230, 230)

    #Запуск основного цикла программы
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        

    


run_game()

