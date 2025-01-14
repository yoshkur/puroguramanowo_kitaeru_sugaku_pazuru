# P.253

from copy import deepcopy
from itertools import product

W, H = 4, 4


def search(pos: int, cells: list, is1x1: bool):
    if pos == W * H:
        if is1x1:
            return [1, 0]
        else:
            return [1, 1]

    if cells[pos]:
        return search(pos=pos + 1, cells=cells, is1x1=is1x1)

    x, y = pos % W, pos // W
    result = [0, 0]
    for dy, dx in product(range(1, H - y + 1), range(1, W - x + 1)):
        next_cells = deepcopy(cells)
        settable = True
        for h, w in product(range(dy), range(dx)):
            if next_cells[(x + w) + (y + h) * W]:
                settable = False
            else:
                next_cells[(x + w) + (y + h) * W] = True
        if settable:
            res = search(pos=pos + 1, cells=next_cells, is1x1=is1x1 or (dx == 1 and dy == 1))
            result[0] += res[0]
            result[1] += res[1]
    return result


if __name__ == '__main__':
    cells = [False] * W * H
    print(search(pos=0, cells=cells, is1x1=False))
