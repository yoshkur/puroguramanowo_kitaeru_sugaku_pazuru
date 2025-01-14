# P.227

N = 10


def move(bit: int, add: int) -> int:
    base = 0

    for i in range(N):
        if bit & (1 << i) > 0:
            base += i + 1

    a0 = (base + add) // 50
    a1 = (base + add) % 50
    b0 = base // 50
    b1 = base % 50

    a2 = a1 // 10
    a3 = a1 % 10
    b2 = b1 // 10
    b3 = b1 % 10

    a4 = a3 // 5
    a5 = a3 % 5
    b4 = b3 // 5
    b5 = b3 % 5
    return abs(a0 - b0) + abs(a2 - b2) + abs(a4 - b4) + abs(a5 - b5)


def search(bit: int, memo: dict) -> int:
    if bit in memo.keys():
        return memo[bit]

    min_ = 1000
    for i in range(N):
        if bit & (1 << i) == 0:
            min_ = min(min_, move(bit=bit, add=i + 1) + search(bit=bit | (1 << i), memo=memo))
    memo[bit] = min_
    return min_


if __name__ == '__main__':
    memo = {}
    memo[(1 << N) - 1] = 0
    print(search(bit=0, memo=memo))
