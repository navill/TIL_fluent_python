import random

# for i in range(10):
#     a = int(random.expovariate(1 / 10)) + 1
#     print(a)
from collections import namedtuple
from queue import PriorityQueue


def co_test(t_arg):
    temp_value = yield t_arg
    print(t_arg)
    temp_value = yield temp_value
    # print(temp_value)

# a = co_test(10)
# b = co_test(1)
# next(a)
# next(b)
# print(a.send(15))
# print(b.send(1))

nt = namedtuple('Test', 'i')
tempq = PriorityQueue()
for i in range(100):
    nt = random.randint(1,10)
    tempq.put(nt)

for j in range(100):
    print(tempq.get())