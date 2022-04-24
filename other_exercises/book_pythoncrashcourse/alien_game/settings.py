class Settings():
    """Класс для хранения всех настроек игры Alien game"""
    def __init__(self):
        '''Инициализирует настройки игры.'''
        
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #Настройки корабля
        self.ship_speed_factor = 1.5

        #Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #Настройка пришельцев
        self.alien_speed_factor = 1

        

