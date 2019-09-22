from concurrent import futures

# flags에서 사용된 save_flag, get_flag, show, main을 재사용한다.
from flags import save_flag, get_flag, show, main

# 최대 스레드 수
MAX_WORKERS = 20


# 각 스레드에서 이 함수를 이용해 여러 국기를 받는다.
# flags.download_many에서 사용된 for 문 본체 동일
def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    # min(최대 스레드, 리스트의 길이)를 이용해 작업자의 수를 결정한다.
    workers = min(MAX_WORKERS, len(cc_list))
    # with futures.ProcessPoolExecutor() as executor:
    with futures.ThreadPoolExecutor(workers) as executor:
        # map() = 각 함수가 반환한 값을 가져올 수 있는 제너레이터 반환
        # __next__() 호출 -> 각 Future 객체의 result() 메서드 호출
        # Future 객체의 결과를 가져올 수 있다.
        res = executor.map(download_one, sorted(cc_list))
        print(res)
        # <generator object Executor.map.<locals>.result_iterator at 0x1086a96d8>
    return len(list(res))


"""
Future 객체 확인을 위해 executor.map()을 submit과 as_completed로 대체
def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print(f'{future} result: {res}')
            results.append(res)
    return len(results)

output: 
Scheduled for BR: <Future at 0x10b02b4a8 state=running>
Scheduled for CN: <Future at 0x10bb4aef0 state=running>
Scheduled for ID: <Future at 0x10bb5d8d0 state=running>
Scheduled for IN: <Future at 0x10bb5de80 state=pending>
Scheduled for US: <Future at 0x10bb5df28 state=pending>
ID BR CN <Future at 0x10b02b4a8 state=finished returned str> result: BR
<Future at 0x10bb4aef0 state=finished returned str> result: CN
<Future at 0x10bb5d8d0 state=finished returned str> result: ID
US <Future at 0x10bb5df28 state=finished returned str> result: US
IN <Future at 0x10bb5de80 state=finished returned str> result: IN

5 flags downloaded in 1.57s
"""

if __name__ == '__main__':
    main(download_many)
