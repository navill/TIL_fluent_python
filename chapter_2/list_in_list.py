test1 = [['_'] * 3 for i in range(3)]
print(test1)
test1[1][2] = 'X'
print(test1)
test2 = [['_'] * 3] * 3
test2[1][2] = 'X'
print(test2)

a = [1, 2, 3, 4]
b = [5, 6, 7]
print(id(a))
print(a)
a += b
print(id(a))
print(a)