# P.219

M, N = 6, 5


def search(candy: list, color: int, memo: dict):
    if candy == [0] * N:
        return 1
    key = tuple(candy + [color])
    if key in memo.keys():
        return memo[key]

    count = 0
    for i in range(len(candy)):
        if i != color % len(candy):
            if candy[i] > 0:
                candy[i] -= 1
                count += search(candy=candy, color=color + 1, memo=memo)
                candy[i] += 1
    key = tuple(candy + [color])
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(search(candy=[M] * N, color=0, memo=memo))
