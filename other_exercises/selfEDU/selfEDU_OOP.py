# lesson 3
from msilib.schema import Class
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


# lesson 14 пример использования магических методов __add__ __sub__
class Clock:
    __DAY = 86400 #число сикунд в одном дне 

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
        
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int или Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        return Clock(self.seconds + sc)


# lesson 18 пример использования магических методов __getitem__ __setitem__ __delitem__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item): #для Миши вариант
        if 0 <= item < len(self.marks):         
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')



s1 = Student('Саша', [8,7,4,4,7,9])
print(s1.marks[1], s1.name)

s2 = Student('Миша', [10,9,9,8,7,9])
print(s2[1], s2.name, f'Полная коллекция оценок {s2.marks}')
#print(s2[21], s2.name) генерируем исключение


# lesson 19 пример использования магических методов __next__ __iter__

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        #self.value = self.start - self.step

    def __iter__(self):                     #чтобы можно было применить цикл for для итерации прописывается магический метод __iter__
        self.value = self.start - self.step
        return self 

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value +=self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 3, 0.5)

"""print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
# print(fr.__next__()) срабатывает исключение StopIteration"""

"""print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))"""

for i in fr:
    print('Через for', i)


# lesson 20 Наследование от встроенных типов и от object

class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


class Vector2(list):
    pass


v = Vector([1,2,5])
print(v)
print(type(v))

v2 = Vector2([1,2,5])
print(v2)
print(type(v2))