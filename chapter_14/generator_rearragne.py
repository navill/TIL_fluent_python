import itertools

list(itertools.groupby('LLLLAAGGG'))
# [('L', <itertools._grouper object at 0x103084c18>),
# ('A', <itertools._grouper object at 0x103084e48>),
# ('G', <itertools._grouper object at 0x103084e80>)]

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
# L -> ['L', 'L', 'L']
# A -> ['A', 'A']
# G -> ['G', 'G', 'G', 'G']

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals)

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']

list(itertools.tee('ABC'))
# [<itertools._tee object at 0x102f77548>,
# <itertools._tee object at 0x103097448>]
g1, g2 = itertools.tee('ABC')
next(g1)  # 'A'
next(g2)  # 'A'