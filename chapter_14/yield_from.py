from collections import abc


def chain(*iterable):
    for it in iterable:
        print('it:', type(it), it)
        # print(isinstance(it, abc.Iterable))  # -> True

        for i in it:
            print('i:', type(i), i)
            yield i


def chain2(*iterable):
    for i in iterable:
        print('i2:', type(i), i)
        # print(isinstance(i, abc.Iterable))  # -> True
        # yield from이 반복형에게 동작을 위임 -> 위 예제의 안쪽 for 문과 동일한 동작 실행
        yield from i


s = 'ABC'
t = [1, 2, 3]
print(list(chain(s, t)))
print(list(chain2(s, t)))
