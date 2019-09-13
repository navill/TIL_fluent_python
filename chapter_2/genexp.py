symbols = '$¢£¥€¤'
a = (ord(symbol) for symbol in symbols)
b = [ord(symbol) for symbol in symbols]
print(type(a))
print(type(b))
for i in a:
    print(i)