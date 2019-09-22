# 표준 라이브러리 - 가장 위에 임포트
import os
import sys
import time

# 외부 라이브러리 - 한 칸 띄고 임포트
import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = f'{BASE_URL}/{cc.lower}/{cc.lower}.gif'
    resp = requests.get(url)
    # print(resp.content)
    return resp.content


def show(text):
    print(text, end=' ')
    # 일반적으로 파이썬은 개행문자 '\n'를 받기 전까지 화면에 출력하지 않는다.
    # sys.stdout.flush()


def download_many(cc_list):
    # print(cc_list)
    for cc in sorted(cc_list):
        image = get_flag(cc)
        # print(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n{count} flags downloaded in {elapsed:.2f}s')


if __name__ == '__main__':
    main(download_many)
