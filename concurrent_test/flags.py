import os
import time
import sys

import requests  # external library - 관례적으로 내장 라이브러리에서 한 칸 띄운다

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'download_flag/'


def save_flag(img, filename):  # data를 지정된 directory에 저장
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # request를 이용해 사이트로부터 국기.gif 수집
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):  # 화면 출력
    print('a', text, end=' ')
    sys.stdout.flush()
# ----------------------------------------------------


def download_many(cc_list):  # cc_list(POP20_CC)
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
