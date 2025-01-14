# P.287

from itertools import product

W, H = 4, 3
XOR_ROW = (1 << (W + 1)) - 1


def search(up: int, y: int, odds: int):
    if 2 < odds:
        return 0

    row = 1 << W | 1

    if y == 0 or y == H:
        row = XOR_ROW ^ row

    if y == H:
        odds += bin(row ^ up).count('1')
        if odds == 0 or odds == 2:
            return 1
        return 0

    count = 0
    for a, b in product(range(1 << W), range(1 << W)):
        count += search(up=a ^ b << 1, y=y + 1, odds=odds + bin(row ^ up ^ a << 1 ^ b).count('1'))
    return count


if __name__ == '__main__':
    print(search(up=0, y=0, odds=0))
