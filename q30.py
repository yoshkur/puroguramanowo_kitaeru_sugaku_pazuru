# P.125
# 数分経っても終わらない。

N = 20


def set_tap(remain: int):
    if remain == 1:
        return 1

    count = 0

    for i in range(1, remain // 2 + 1):
        if remain - i == i:
            count += set_tap(remain=i) * (set_tap(remain=i) + 1) // 2
        else:
            count += set_tap(remain=remain - i) * set_tap(remain=i)

    for i in range(1, remain // 3 + 1):
        for j in range(i, (remain - i) // 2 + 1):
            if remain - (i + j) == i and i == j:
                count += set_tap(remain=i) * (set_tap(remain=i) + 1) * (set_tap(remain=i) + 2) // 6
            elif remain - (i + j) == i:
                count += set_tap(remain=i) * (set_tap(remain=i) + 1) * set_tap(remain=j) // 2
            elif i == j:
                count += set_tap(remain=remain - (i + j)) * set_tap(remain=i) * (set_tap(remain=i) + 1) // 2
            elif remain - (i + j) == j:
                count += set_tap(remain=j) * (set_tap(remain=j) + 1) * set_tap(remain=i) // 2
            else:
                count += set_tap(remain=remain - (i + j)) * set_tap(remain=j) * set_tap(remain=i)
    return count


if __name__ == '__main__':
    print(set_tap(remain=N))
