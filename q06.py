# P.35

def is_arrange_colats(target_value: int):
    value = target_value * 3 + 1
    while True:
        if value == 1:
            return False
        if value == target_value:
            return True

        if value % 2:
            value = value * 3 + 1
        else:
            value /= 2


if __name__ == '__main__':
    count = 0
    for i in range(2, 10001, 2):
        if is_arrange_colats(target_value=i):
            count += 1
    print(count)
