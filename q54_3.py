# P.223

N = 11


def search(cards: int, num: int, memo: dict):
    if num == 0:
        return 1
    if cards in memo.keys():
        return memo[cards]

    mask = (1 << (num + 1)) + 1
    count = 0
    while mask < (1 << (N * 2)):
        if cards & mask == 0:
            count += search(cards=cards | mask, num=num - 1, memo=memo)
        mask <<= 1
    memo[cards] = count
    return count


if __name__ == '__main__':
    memo = {}

    print(search(cards=0, num=N, memo=memo))
