"""
Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
"""

class NewType(type):
    atr = None
    @classmethod
    def __prepare__(metacls, name, bases):
        return type.__prepare__(metacls, name, bases)

    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(NewType, cls).__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        if cls.atr is None:
            cls.atr = super().__call__(*args, **kwargs)
        return cls.atr

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr


class MyClass(metaclass=NewType):
    atribut = " "

a = MyClass()
b = MyClass()

print(a is b) 
print(a == b)