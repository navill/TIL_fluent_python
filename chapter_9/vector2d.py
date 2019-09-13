# vector2d.py
import math
from array import array


class Vector2d:
    typecode = 'd'
    # 아래의 속성들이 이 클래스에 속함을 인터프리터에게 제공한다.
    # 인터프리터는 이 속성들을 각 객체의 튜플형 구조체에 저장한다.
    __slots__ = ('__x', '__y')
    # 만일 __slots__을 정의한 상태에서 이 객체를 약한 참조로 사용하고 싶을 경우
    # __weakref__ 속성을 slots 리스트에 추가해야한다.

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property  # __hash__() 구현을 위해 @property를 이용하여 x,y를 읽기 전용으로 만든다
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        # 요소의 hash에 XOR('^') 연산자를 권장
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


v1 = Vector2d(3, 4)
v2 = Vector2d(3.3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
octets = bytes(v1)
print(octets)
print(abs(v1))
# @classmethod 데커레이터에 의해 frombytes를 실행하기 위해 Vector2d class에 직접 접근할 수 있다.
print(Vector2d.frombytes(octets))
print(hash(v1), hash(v2))
print(set([v1, v2]))
