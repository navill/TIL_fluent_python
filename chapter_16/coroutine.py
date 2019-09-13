def simple_coroutine():
    print(f'start coroutine')
    x = yield  # 1
    print(f'coroutine receives value -> {x}')


sc = simple_coroutine()
# next에 의해 # 1(변수 x에 할당되기 전)까지 실행
next(sc)


# send에 의해 yield에 4가 전달되고 x에 4가 할당된다.
# sc.send(4)  # 제어 흐름이 끝까지 도달했으므로 일반적인 제너레이터처럼 StopIteration 발생


def simple_coroutine2(a):
    print(f'start coroutine -> {a}')
    b = yield a
    print(f'coroutine receives b value -> {b}')
    # print(a)
    c = yield a + b
    print(f'coroutine receives c value -> {c}')


from inspect import getgeneratorstate

sc2 = simple_coroutine2(4)
print(getgeneratorstate(sc2))  # GEN_CREATED
next(sc2)
print(getgeneratorstate(sc2))  # GEN_SUSPENDED
print(sc2.send(5))
# -> coroutine receives value -> 5
# -> 9 (9는 yield a+b에 의해 생성되고 아래의 send(2)에 의해 c 변수에 2가 할당된다.)
print(sc2.send(2))
# coroutine receives value -> 2
#     print(sc2.send(2))
# StopIteration
print(getgeneratorstate(sc2))  # GEN_CLOSED : 실제로 화면에 출력되지 않는다.
# 파이썬 버전이 달라서 실행에 약간의 차이가 있는듯
