"""
Класс, который принимает объект в качестве аргумента
и проводит интроспекцию
"""
from pprint import pprint
import inspect


class Introspection:

    def __init__(self, x):
        self.x = x

    def introspection_info(self):
        print(type(self.x))
        pprint(dir(self.introspection_info))
        pprint(dir(self.x))
        print(hasattr(self.introspection_info, 'x'))

    def class_method_module(self):
        where_class_method_module = inspect.getmodule(some_object.class_method_module)
        print(where_class_method_module)


# Выводит тип атрибута, доступные атрибуты и методы функции, доступные атрибуты и методы атрибута,
# существует ли атрибут 'х' в функции, существует ли функция в модуле и где
some_object = Introspection(111)
some_object.introspection_info()
some_object.class_method_module()
