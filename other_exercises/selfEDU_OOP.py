# lesson 3
from string import ascii_letters
from typing import Type


class Point:
    color = 'red'
    cercle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt.__dict__)


# lesson 4
class Point:
    def __new__(cls, *args, **kwargs):
        print('вызов __new__ для ' + str(cls))
    
    def __init__(self, x=0, y=0):
        print('вызов __init__ для ' + str(self))
        self.x = x
        self.x = y


pt = Point(1, 2)


# lesson 10 пример использования объектов property
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.__fio = fio.split()
        self.__old = old
        self.__pasport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть стркой')
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) !=0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')


p = Person('Балакирев Сергей Михайлович', 30, '1234 567890', 80.0)

