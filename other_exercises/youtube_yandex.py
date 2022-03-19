class Myclass:
    class_attribute = 'I am a class attribute'

    def __init__(self, param1, param2):
        self.param1 = param1
        self.custom_name = param2
        self.name = 'world'

    def say_hello(self):
        return 'hello ' + self.name


instance = Myclass('abc', 42)
id(instance)
instance.say_hello()
instance.param1
instance.class_attribute

#-----
class Speedometer:
    def __init__(self, max_speed, units):
        print('__init__')
        self.max_speed = max_speed
        self.units = units

    def __new__(cls, max_speed, units):
        print('__new__')
        if max_speed > 250:
            return None
        return super().__new__(cls)


s1 = Speedometer(200, 'km')
s1.max_speed
s2 = Speedometer(350, 'miles')
s2 is None

#-----
class Pizza:
    def __init__(self, size):
        self.size = size

    @classmethod
    def get_large_pizza(cls):
        return cls(42)
    
    @classmethod
    def get_standart_pizza(cls):
        return cls(30)


large_pizza = Pizza.get_large_pizza()
large_pizza.size
standart_pizza = Pizza.get_standart_pizza()
standart_pizza.size


#----- 