class CoroException(Exception):
    pass


def coro_exception_handling():
    print('coroutine start')
    try:
        while True:
            try:
                x = yield
            except CoroException:
                print('raised exception, but function is not terminated')
            else:
                print(f'coroutine received -> {x}')
    finally:
        print('end coroutine')
    # 이 코루틴은 반드시 예외 처리에 의해서만 종료(while 종료)될 수 있으므로
    # 아래의 raise 구문은 실행될 수 없다.
    raise RuntimeError('??')


ceh = coro_exception_handling()
next(ceh)
ceh.send(10)
# throw를 이용해 예외를 던져도 해당 구문이 종료되지 않는다.
ceh.throw(CoroException)  # raised exception, but function is not terminated
# 해당하지 않는 예외를 던질 경우 코루틴은 종료된다.
# ceh.throw(ZeroDivisionError)
# ...
# ZeroDivisionError
