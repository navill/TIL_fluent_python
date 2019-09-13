import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    print(i)
    return grades[i]


print([grade(score) for score in [33, 70, 55, 40, 77, 70, 89, 90, 100]])

a = tuple()
print(dir(a))
b = list()
print(dir(b))