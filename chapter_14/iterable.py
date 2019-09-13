# # from collections import abc
# #
# #
# # class Foo:
# #     def __iter__(self):
# #         pass
# #
# #
# # class Bar:
# #     def __getitem__(self, item):
# #         pass
# #
# #
# # f = Foo()
# # b = Bar()
# #
# # print(issubclass(Foo, abc.Iterable))  # True
# # print(isinstance(f, abc.Iterable))  # True
# # print(isinstance(Bar, abc.Iterable))  # False
# # print(isinstance(b, abc.Iterable))  # False
# # print(dir(b))
# #
# # s = 'ABC'
# # it = iter(s)
# # while True:
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         del it
# #         break
# #
# # import re
# # import reprlib
# # from collections import abc
# #
# # RE_WORD = re.compile('\w+')
# #
# #
# # class Sentence:
# #     def __init__(self, text):
# #         self.text = text
# #         self.words = RE_WORD.findall(text)
# #
# #     def __repr__(self):
# #         return 'Sentence(%s)' % reprlib.repr(self.text)
# #
# #     def __iter__(self):
# #         return SentenceIterator(self.words)
# #
# #
# # class SentenceIterator:
# #     def __init__(self, words):
# #         self.words = words
# #         self.index = 0
# #
# #     def __next__(self):
# #         try:
# #             word = self.words[self.index]
# #         except IndexError:
# #             raise StopIteration()
# #         self.index += 1
# #         return word
# #
# #     def __iter__(self):
# #         return self
# #
# #
# # s = Sentence('i am your friend')
# # it = iter(s)
# # print(dir(s))
# # print(dir(it))
# # it2 = iter(s)
# # print(id(it))
# # print(id(it2))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# #
# # print(issubclass(Sentence, abc.Iterable))
# # print(isinstance(s, abc.Iterable))
# # print(isinstance(it, abc.Iterator))
# #
# #
# # class Sentence:
# #     def __init__(self, text):
# #         self.text = text
# #
# #     def __repr__(self):
# #         return 'Sentence(%s)' % reprlib.repr(self.text)
# #
# #     def __iter___(self):
# #         # finditer = 단어에 대응되는 반복자(MatchObject) 객체 생성
# #         for match in RE_WORD.finditer(self.text):
# #             yield match.group()
# #
# #
# # import itertools
# #
# #
# # def aritprog_gen(begin, step, end=None):
# #     first = type(begin + step)(begin)
# #     ap_gen = itertools.count(first, step)
# #     if end is not None:
# #         ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
# #     return ap_gen
# #
# # gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
# # print(list(gen))
# # # output:
# # [1, 1.5, 2.0, 2.5]
# #
# # arit = aritprog_gen(0,2,10)
# # for i in arit:
# #     print(i)
#
# def vowel(c):
#     return c.lower() in 'aeiou'
#
#
# list(filter(vowel, 'Aardvark'))
# import itertools
#
# print(list(itertools.filterfalse(vowel, 'Aardvark')))
# print(list(itertools.dropwhile(vowel, 'Aardvark')))
# print(list(itertools.takewhile(vowel, 'Aardvark')))
# print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
# print(list(itertools.islice('Aardvark', 4)))
# print(list(itertools.islice('Aardvark', 4, 7)))
# print(list(itertools.islice('Aardvark', 1, 7, 2)))
#
# # itertools.accumulate 예제
# sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
# import itertools
#
# list(itertools.accumulate(sample))  # [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
# list(itertools.accumulate(sample, min))  # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
# list(itertools.accumulate(sample, max))  # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
# import operator
#
# list(itertools.accumulate(sample, operator.mul))  # [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
#
# list(enumerate('albatroz', 1))
# # [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]
# import operator
#
# list(map(operator.mul, range(11), range(11)))
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list(map(operator.mul, range(11), [2, 4, 8]))
# # [0, 4, 16]
# list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))
# [(0, 2), (1, 4), (2, 8)]
# import itertools
#
# list(itertools.starmap(operator.mul, enumerate('albatroz',
#                                                1)))  # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
#
# sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
# print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))
# # [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
# # 5.0, 4.375, 4.888888888888889, 4.5]
# for i in enumerate(itertools.accumulate(sample), 1):
#     print(i)
#
# print(list(itertools.chain('ABC', range(2)))) # ['A', 'B', 'C', 0, 1]
# print(list(itertools.chain(enumerate('ABC')))) # [(0, 'A'), (1, 'B'), (2, 'C')]
# print(list(itertools.chain.from_iterable(enumerate('ABC')))) # [0, 'A', 1, 'B', 2, 'C']
# print(list(zip('ABC', range(5)))) #
# # [('A', 0), ('B', 1), ('C', 2)]
# print(list(zip('ABC', range(5), [10, 20, 30, 40]))) #
# # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
# print(list(itertools.zip_longest('ABC', range(5)))) #
# # [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
# print(list(itertools.zip_longest('ABC', range(5), fillvalue='?'))) # [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
# print(list(itertools.product('ABC', range(2))))
# # [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
# suits = 'spades hearts diamonds clubs'.split()
# print(list(itertools.product('AK', suits)))
# # [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
# print(list(itertools.product('ABC')))
# # [('A',), ('B',), ('C',)]
# print(list(itertools.product('ABC', repeat=2))) #
# # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# # ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# print(list(itertools.product(range(2), repeat=3)))
# # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
# rows = itertools.product('AB', range(2), repeat=2)
# for row in rows:
# 		print(row)
#
import itertools
import operator

ct = itertools.count()
next(ct)  #
next(ct), next(ct), next(ct)
# (1, 2, 3)
list(itertools.islice(itertools.count(1, .3), 3))
# [1, 1.3, 1.6]
cy = itertools.cycle('ABC')
next(cy)
# 'A'
list(itertools.islice(cy, 7))
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']
rp = itertools.repeat(7)
next(rp), next(rp)
# (7, 7)
list(itertools.repeat(8, 4))
# [8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5)))
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

list(itertools.combinations('ABC', 2))  #
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations_with_replacement('ABC', 2))  #
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.permutations('ABC', 2))  #
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
list(itertools.product('ABC', repeat=2))  #
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

list(itertools.tee('ABC'))
# [<itertools._tee object at 0x102f77548>, <itertools._tee object at 0x103097448>]
g1, g2 = itertools.tee('ABC')
next(g1)  # 'A'
next(g2)  # 'A'

list(itertools.groupby('LLLLAAGGG'))  #

for char, group in itertools.groupby('LLLLAAAGG'):  #
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals)

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
