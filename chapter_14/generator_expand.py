import itertools
import operator

"""
순열 조합 - combinations, combinations_with_replacement, permutations, product
"""
list(itertools.combinations('ABC', 2))  # 중복 X
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.permutations('ABC', 2))  # 항목들 간에 순서 O
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
list(itertools.combinations_with_replacement('ABC', 2))  # 중복 O, 교차 허용 X
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.product('ABC', repeat=2))  # 중복 O, 교차 허용 O
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

"""
count, repeat : 반복형을 인수로 받지 않고, 반복형을 생성한다.
cycle : 반복형을 (느긋하게)무한히 반복한다.
"""
ct = itertools.count()
next(ct)  # 0
# 튜플을 생성하는 것은 ()가 아니라 쉼표(,)를 기준으로 생성
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