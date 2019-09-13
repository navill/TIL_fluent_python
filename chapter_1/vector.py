from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # from repr()
    def __repr__(self):
        return f'Vector({self.x:.2f}, {self.y:.2f})'

    # from abs()
    def __abs__(self):
        return hypot(self.x, self.y)

    # bool()
    def __bool__(self):
        return bool(abs(self))

    # add() or '+'
    # x = A객체.x + B객체.x => vector1 + vector2 연산이 가능해진다.
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # 새로운 Vector 객체 생성 - 두 개의 피 연산자는 변경하지 않는다.
        return Vector(x, y)

    # mul() or '*'
    # Vector(백터 객체.x * scalar, 백터 객체.y *scalar) => vector1 * 2 연산이 가능해진다
    def __mul__(self, scalar):
        # 새로운 Vector 객체 생성
        return Vector(self.x * scalar, self.y * scalar)


v0 = Vector(0, 0)
print(bool(v0))  # 벡터의 크기가 0일 경우, False
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)  # Vector(4.000, 5.000)

v = Vector(3, 4)
print(v * 3)  # Vector(9.000, 12.000)
print(abs(v * 3))  # 15.0
print(bool(v))
