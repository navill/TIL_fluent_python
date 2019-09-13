def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # count += 1  # count에 할당되는 순간 새로운 객체 생성 -> free variable이 해제된다.
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
