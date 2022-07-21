# Exercise 2
# Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер.
# Код для проверки правильности решения:


class Meta(type):
    children_number = 0

    def __new__(mcs, name, base, attrs):
        attrs.update({'class_number': mcs.children_number})
        mcs.children_number += 1
        return type.__new__(mcs, name, base, attrs)

    # def __call__(cls, *args, **kwargs):
    #     return super().__call__(*args, **kwargs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
