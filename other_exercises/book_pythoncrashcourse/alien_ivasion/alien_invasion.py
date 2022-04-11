import sys
import pygame
from settings import Settings


def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien game')
    #Назначение цвета фона
    bgcolor = (230, 230, 230)

    #Запуск основного цикла программы
    while True:
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #При каждом проходе цикла перересовывается экран
            screen.fill(ai_settings.bg_color)
        
        #Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()

