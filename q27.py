# P.113

import copy

W, H = 6, 4
DIR = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def search(x, y, dir, left, bottom):
    left_l = copy.copy(left)
    bottom_l = copy.copy(bottom)
    if dir == 0 or dir == 2:
        pos = min([y, y + DIR[dir][1]])
        if pos < 0 or y + DIR[dir][1] > H:
            return 0
        if len(left_l) > pos and left_l[pos] & (1 << x) > 0:
            return 0
        left_l[pos] |= (1 << x)
    else:
        pos = min([x, x + DIR[dir][0]])
        if pos < 0 or x + DIR[dir][0] > W:
            return 0
        if len(bottom_l) > pos and bottom_l[pos] & (1 << y) > 0:
            return 0
        bottom_l[pos] |= (1 << y)
    next_x, next_y = x + DIR[dir][0], y + DIR[dir][1]
    if next_x == W and next_y == H:
        return 1

    count = 0
    count += search(x=next_x, y=next_y, dir=dir, left=left_l, bottom=bottom_l)
    dir = (dir + 1) % len(DIR)
    count += search(x=next_x, y=next_y, dir=dir, left=left_l, bottom=bottom_l)
    return count


if __name__ == '__main__':
    left = [0] * H
    bottom = [0] * W
    print(search(x=0, y=0, dir=3, left=left, bottom=bottom))
