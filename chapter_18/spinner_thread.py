# # # import asyncio
# # # import itertools
# # # import sys
# # # from inspect import getgeneratorstate
# # #
# # # # # example 18-1
# # # # class Signal:  # 1 가변 객체 정의
# # # #     # 외부에서 이 객체의 속성을 수정함으로써 특정 함수나 순환문을 중단시킬 수 있다.
# # # #     go = True
# # # #
# # # #
# # # # def spin(msg, signal):  # 2 이 함수는 별도의 스레드에서 실행.
# # # #     write, flush = sys.stdout.write, sys.stdout.flush
# # # #     for char in itertools.cycle('|/=\\'):  # 3 무한루프
# # # #         status = char + ' ' + msg
# # # #         write(status)
# # # #         flush()
# # # #         # 4 애니메이션 기법 - 문자열의 길이만큼 백스페이스 문자를 반복 해서 커서 이동
# # # #         write('\x08' * len(status))
# # # #         time.sleep(.1)
# # # #         # 5 기저 조건
# # # #         if not signal.go:
# # # #             break
# # # #     # 6 공백 문자로 덮어쓰기 + 커서 이동
# # # #     write(' ' * len(status) + '\x08' * len(status))
# # # #
# # # #
# # # # def slow_function():  # 7
# # # #     # 8 메인 스레드에서 sleep 호출할 때, GIL 해제 -> 두 번째 스레드 진행
# # # #     time.sleep(3)
# # # #     return 42
# # # #
# # # #
# # # # def supervisor():  # 9 두 번째 스레드 생성
# # # #     signal = Signal()
# # # #     # target = 실행할 함수
# # # #     # args = 실행될 함수의 매개 변수
# # # #     spinner = threading.Thread(target=spin, args=('thinking!', signal))
# # # #     print('spinner object:', spinner)  # 10 두 번째 스레드 객체 출력
# # # #     spinner.start()  # 11 두 번째 스레드 실행
# # # #     result = slow_function()  # 12 주 스레드 블로킹, 두 번째 스레드의 스피너 애니메이션 실행
# # # #     signal.go = False  # 13 spin() for 중단
# # # #     spinner.join()  # 14 spinner 스레드가 끝날 때까지 대기
# # # #     return result
# # # #
# # # #
# # # # def main():
# # # #     result = supervisor()  # 15
# # # #     print('Answer:', result)
# # # #
# # #
# # # """
# # # 파이썬에는 스레드를 종료시키는 API가 정의되어 있지 않다.
# # # -> 메시지를 보내 종료시켜야 한다(signal.go).
# # # """
# # #
# # #
# # # # example 18-2
# # # # @asyncio.coroutine  # 1
# # # async def spin2(msg):  # 2
# # #     write, flush = sys.stdout.write, sys.stdout.flush
# # #     for char in itertools.cycle(('|/-\\')):
# # #         status = char + ' ' + msg
# # #         write(status)
# # #         flush()
# # #         write('\x08' * len(status))
# # #         try:
# # #             # yield from asyncio.sleep(.1)  # 3
# # #             await asyncio.sleep(.1)
# # #         except asyncio.CancelledError:  # 4 <- # 11에 의해 CancelledError가 발생된다.
# # #             break
# # #     write(' ' * len(status) + '\x08' * len(status))
# # #
# # #
# # # @asyncio.coroutine
# # # def slow_function2():  # 5
# # #     yield from asyncio.sleep(3)  # 6 <- 1~4가 실행되는동안(3초) 대기
# # #     return 42
# # #
# # #
# # # # @asyncio.coroutine
# # # async def supervisor2():  # 7
# # #     # asyncio.async(deprecated) -> asyncio.create_task
# # #     # getgeneratorstate(spin2)
# # #     spinner = asyncio.create_task(spin2('thinking!'))  # 8 Task 객체 반환
# # #     print('spinner object:', spinner)  # 9
# # #     result = await slow_function2()  # 10 -> #6이 모두 실행되면 다음행(#11)으로 진행
# # #     # 이벤트 루프(#3)는 계속해서 실행된다
# # #
# # #     spinner.cancel()  # 11
# # #     return result
# # #
# # #
# # # def main2():
# # #     loop = asyncio.get_event_loop()  # 12
# # #     result = loop.run_until_complete(supervisor2())  # 13
# # #     loop.close()
# # #     print('Answer:', result)
# # #
# # #
# # # if __name__ == '__main__':
# # #     # main()
# # #     main2()
# #
# #
# # """
# # python의 특성상 generator는 구조에 따라 stack frame에서 사라지지 않을 수 있다
# # -> 아래의 예문에서 average 실행은 StopIteration 발생 전 까지 메모리에 변수들이 남아있다.
# # -> 지역변수로 total, average, count를 이용할 수 있다.
# # """
# # from functools import wraps
# #
# #
# # def coroutine2(func):
# #     @wraps(func)
# #     def primer(*args, **kwargs):
# #         gen = func(*args, **kwargs)
# #         next(gen)
# #         return gen
# #     return primer
# #
# #
# # # coroutine(기동자 생성) 데커레이터를 이용해 next를 사용하지 않고 코루틴을 사용할 수 있다.
# # @coroutine2
# # def averager():
# #     total = 0.0
# #     average = None
# #     count = 0
# #     while True:
# #         term = yield average
# #         total += term
# #         count += 1
# #         average = total / count
# #
# #
# # coro_avg = averager()
# # # next(coro_avg)  # yield 전까지 실행시키기 위해 send를 이용해 호출자(generator 객체)를 호출해야한다.
# # # - coroutine priming(코루틴 기동) 데커레이터를 이용해 생략시킬 수 있다.
# # print(coro_avg.send(10))
# # print(coro_avg.send(20))
# # print(coro_avg.send(30))
# t1 = (1,2,[10,20])
# t2 = (1,2,[10,20])
# print(t1)
# print(id(t1))
# print(t2)
# print(id(t2))
# t2[-1].append(30)
# print(t2)
# print(id(t2))
#

import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)  # 1
print(ender.alive)  # 2
del s1
print(ender.alive)  # 3
print(ender.peek())  # ({1, 2, 3}, <function bye at 0x10773e1e0>, (), {})
s2 = 'spam'  # 이 시점에서 {1, 2, 3}을 참조하는 객체는 0이 된다. -> finalize의 bye() 실행
print(ender.peek())
print(ender.alive)  # 4


import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)
