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
