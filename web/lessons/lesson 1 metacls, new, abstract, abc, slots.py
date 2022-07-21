# def meta_func(name, bases, attrs):
#     print('meta function called with', name, bases, attrs)
#     attrs["always_add"] = 42
#     return type(name, bases, attrs)
#
#
# class Kls(metaclass=meta_func):
#     some = 2
#
#     def print_some(self):
#         print(self.some)
#
#
# print(Kls.always_add)

# class MyMeta(type):
#     def __new__(*args):
#         print(f'MyMeta __new__ called with {args}')
#         return type.__new__(*args)
#
#     def __init__(*args):
#         print(f'MyMeta __init__ called with {args}')
#
#
# class A(metaclass=MyMeta):
#     def __init__(self, data):
#         self.data = data
#
# a = A('afda')

# class MyMeta(type):
#
#     def __call__(cls, *args):
#         print('MyMeta __call__ called')
#         print('class:', cls)
#         print('args:', args)
#         instance = object.__new__(cls)
#         instance.__init__(*args)
#         return instance
#
#
# class Kls(metaclass=MyMeta):
#
#     def __init__(self, data):
#         print("I am Kls method __init__")
#         self.data = data
#
#     def printd(self):
#         print(self.data)
#
#
# ik = Kls('arun')

# class Kls:
#     def __new__(cls, *args):
#         print(f"Kls method __new__ called with {args}")
#         return super().__new__(cls)
#
#     def __init__(self, data):
#         self.data = data
#
#     def printd(self):
#         print(self.data)
#
#
# ik = Kls('arun')  # Kls method __new__ called with ('arun',)
# ik.printd()  # arun

import types
from functools import wraps


def decorator(func):
    """It`s decorator"""

    @wraps(func)
    def inner(*args, **kwargs):
        """It`s inner in decorator"""
        print(f"It`s a decoratoor {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return inner


class MetaClass(type):
    def __new__(mcs, name, bases, attr):
        """It`s new MetaClass"""
        for key, value in attr.items():
            if isinstance(value, (types.FunctionType, types.MethodType)):
                attr[key] = decorator(value)

        return super(MetaClass, mcs).__new__(mcs, name, bases, attr)


class Math(metaclass=MetaClass):
    def __init__(self, a, b):
        """It`s init Math"""
        self.num1 = a
        self.num2 = b

    def sum_num(self):
        """It`s sum Math"""
        return f'Sum {self.num1 + self.num2}'


m = Math(1, 2)
print('------')
print(m.sum_num())
print('------')
print(m.__init__.__doc__)
print('------')
print(m.sum_num.__doc__)

class Final(type):
    def __new__(mcs, name, bases, attr):
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            if i is Final:
                raise ValueError("It's impossible to be subclass of Final")
        return super(Final, mcs).__new__(mcs, name, bases, attr)


class A(metaclass=Final):
    def show(self):
        print('Hey A')


# class B(A):
#     def show2(self):
#         print("Hey B")


a = A()
# b = B()
