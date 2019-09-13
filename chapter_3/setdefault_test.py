dic = {
    'a': [(1, 2, 3), (1, 2, 3)],
    'b': [(2, 3), (4, 5)],
    'c': [(3), (4), (5)],
}

a = dic.setdefault('d', []).append((4, 5, 6))
print(a)
dic['a'].append((1, 2, 3))
print(dic)
# {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5], 'd': [(4, 5, 6)]}


import collections
import re
import sys

WORD_RE = re.compile('\w+')
# defaultdict(생성자) -> defaultdict 객체 생성
# index.default_factory속성에 기본값(list())이 저장된다.
# -> 이 기본값은 __getitem__() 호출 시 사용된다.
index = collections.defaultdict(list)

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])


class StrKeyDict0(dict):
    def __missing__(self, key):
        # key가 문자열로서 존재하지 않을경우 KeyError
        if isinstance(key, str):  # 2, # 4
            raise KeyError(key)  # 5
        return self[str(key)]  # 3

    def get(self, key, default=None):
        try:
            return self[key]  # 1
        except KeyError:
            # key가 없을 경우
            return default  # 6

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# d[1]  # error
print(d.get('2'))
print(d.get(4))
#
print(d.get(0))
print(d.get('0', 'zero'))
# print()


import collections

import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# d[1]  # error
print(d.get('2'))  # two
print(d.get(4))  # four
print(d.get(0))  # None
print(d.get(0, 'zero'))  # zero

s = frozenset((0, 1, 2, 3)) | set((2, 3, 4, 5))
y = set((2, 3, 4, 5)) | frozenset((0, 1, 2, 3))
print(type(s))
print(type(y))