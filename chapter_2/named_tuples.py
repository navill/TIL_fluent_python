from collections import namedtuple, OrderedDict

# 명명된 튜플(namedtuple)은 클래스 명과 필드명으로 구성된 리스트(반복형 문자열(?) 또는
# 공백으로 구성된 문자열)
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])

print(City._fields)  # ._field = 클래스의 필드명
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # ._make(iter) = City(*delhi_data)와 동일
print(delhi._asdict())  # _asdict() = OrderedDict 생성
for key, value in delhi._asdict().items():
    print(key + ':', value)