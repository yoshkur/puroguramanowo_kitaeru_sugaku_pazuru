# P.261

from itertools import combinations


W, H = 5, 4


def check(color: list, del_: int):
    color.remove(del_)
    left, right, up, down = del_ - 1, del_ + 1, del_ - W, del_ + W
    if del_ % W > 0 and left in color:
        check(color=color, del_=left)
    if del_ % W != W - 1 and right in color:
        check(color=color, del_=right)
    if del_ // W > 0 and up in color:
        check(color=color, del_=up)
    if del_ // W != H - 1 and down in color:
        check(color=color, del_=down)


if __name__ == '__main__':
    map_ = list(range(W * H))
    count = 0
    for blue in combinations(iterable=map_, r=W * H // 2):
        blue = list(blue)
        if 0 in blue:
            white = list(set(map_) - set(blue))
            check(color=blue, del_=blue[0])
            if len(blue) == 0:
                check(color=white, del_=white[0])
            if len(white) == 0:
                count += 1
    print(count)
