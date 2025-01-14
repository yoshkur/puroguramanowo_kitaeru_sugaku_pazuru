# P.301

from itertools import product


W, H = 5, 6

ALL = (1 << W) - 1


def check(r1: int, r2: int, r3: int) -> bool:
    result = True
    for i in range(W):
        m1 = (0b111 << (i - 1) if i > 0 else 3) & ALL
        m2 = 1 << i
        if r1 & m2 == m2 and r2 & m1 == m1 and r3 & m2 == m2:
            result = False
        if (r1 ^ ALL) & m2 == m2 and (r2 ^ ALL) & m1 == m1 and (r3 ^ ALL) & m2 == m2:
            result = False

    return result


def search(pre1: int, pre2: int, line: int, used: int, boys: list, next_: dict, memo: dict) -> int:
    if (pre1, pre2, line, used) in memo.keys():
        return memo[(pre1, pre2, line, used)]

    if line >= H:
        memo[(pre1, pre2, line, used)] = 1 if used == W * H // 2 else 0
        return memo[(pre1, pre2, line, used)]

    result = 0
    if line == H - 1:
        for row in next_[(pre2, pre1)]:
            if pre1 in next_[(row, row)] and used + boys[row] <= W * H // 2:
                result += search(pre1=row, pre2=pre1, line=line + 1, used=used + boys[row], boys=boys, next_=next_, memo=memo)
    else:
        for row in next_[(pre2, pre1)]:
            if used + boys[row] <= W * H // 2:
                result += search(pre1=row, pre2=pre1, line=line + 1, used=used + boys[row], boys=boys, next_=next_, memo=memo)
    memo[(pre1, pre2, line, used)] = result
    return result


if __name__ == '__main__':
    boys = [bin(i).count('1') for i in range(ALL + 1)]

    next_ = {}
    for r1, r2 in product(range(1 << W), range(1 << W)):
        next_[(r1, r2)] = [r3 for r3 in range(ALL + 1) if check(r1=r1, r2=r2, r3=r3)]

    memo = {}

    count = 0

    for r0 in range(1 << W):
        count += search(pre1=r0, pre2=r0, line=1, used=boys[r0], boys=boys, next_=next_, memo=memo)

    print(count)
