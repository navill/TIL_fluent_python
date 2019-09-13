colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 지능형 리스트에서 반복문을 두 번 쓸경우 줄바꿈함으로써 가독성을 높일 수 있다.
# 아래의 코드는 사이즈를 반복한 후 색상을 매칭한다.
# 둘의 위치(color 반복문과 size 반복문)를 변경할 경우,
# 색상을 반복 한 후 사이즈를 반복한다.
complist_tshirts = [(color, size) for color in colors
           for size in sizes]
genexp_tshirts = ((color, size) for color in colors
           for size in sizes)
print(complist_tshirts)
for i in genexp_tshirts:
    print(i)