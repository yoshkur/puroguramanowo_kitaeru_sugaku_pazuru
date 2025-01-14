# P.125

N = 20


def set_tap(remain: int, memo: dict):
    if remain in memo.keys():
        return memo[remain]

    count = 0

    for i in range(1, remain // 2 + 1):
        if remain - i == i:
            count += set_tap(remain=i, memo=memo) * (set_tap(remain=i, memo=memo) + 1) // 2
        else:
            count += set_tap(remain=remain - i, memo=memo) * set_tap(remain=i, memo=memo)

    for i in range(1, remain // 3 + 1):
        for j in range(i, (remain - i) // 2 + 1):
            if remain - (i + j) == i and i == j:
                count += set_tap(remain=i, memo=memo) * (set_tap(remain=i, memo=memo) + 1) * (set_tap(remain=i, memo=memo) + 2) // 6
            elif remain - (i + j) == i:
                count += set_tap(remain=i, memo=memo) * (set_tap(remain=i, memo=memo) + 1) * set_tap(remain=j) // 2
            elif i == j:
                count += set_tap(remain=remain - (i + j), memo=memo) * set_tap(remain=i, memo=memo) * (set_tap(remain=i, memo=memo) + 1) // 2
            elif remain - (i + j) == j:
                count += set_tap(remain=j, memo=memo) * (set_tap(remain=j, memo=memo) + 1) * set_tap(remain=i, memo=memo) // 2
            else:
                count += set_tap(remain=remain - (i + j), memo=memo) * set_tap(remain=j, memo=memo) * set_tap(remain=i, memo=memo)
    memo[remain] = count
    return count


if __name__ == '__main__':
    memo = {1: 1}
    print(set_tap(remain=N, memo=memo))
