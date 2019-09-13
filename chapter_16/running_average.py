from collections import namedtuple
from functools import wraps


# decorator for coroutine priming
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


Result = namedtuple('Result', 'count average')


@coroutine
def running_avg():
    total = 0.0
    count = 0
    average = None
    while True:
        # 무한 루프이므로 호출자가 값을 보내줄때마다 계속해서 연산 진행
        # del을 이용해 가비지 컬렉트되거나 호출자가 close() 메서드를 호출하면 종료됨
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
        # Result()
    return Result(count, average)


ra = running_avg()
# next(ra)  # 코루틴 기동(priming)
# @coroutine을 사용할 경우 사용되지 않는다.
print(ra.send(10))  # 10.0
print(ra.send(15))  # 12.5
print(ra.send(20))  # 15
try:
    ra.send(None)
except StopIteration as exc:
    result = exc.value
print(result)
