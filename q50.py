# P.207

W, H = 6, 5
USABLE = 2


def search(x: int, y: int, h: list, v: list):
    global max_

    if x == W and y == H:
        max_ = max([sum(h) + sum(v), max_])
        return

    if h[y] < USABLE:
        if x > 0:
            h[y] += 1
            search(x=x - 1, y=y, h=h, v=v)
            h[y] -= 1
        if x < W:
            h[y] += 1
            search(x=x + 1, y=y, h=h, v=v)
            h[y] -= 1
    if v[x] < USABLE:
        if y > 0:
            v[x] += 1
            search(x=x, y=y - 1, h=h, v=v)
            v[x] -= 1
        if y < H:
            v[x] += 1
            search(x=x, y=y + 1, h=h, v=v)
            v[x] -= 1


if __name__ == '__main__':
    max_ = 0
    h = [0] * (H + 1)
    v = [0] * (W + 1)

    search(x=0, y=0, h=h, v=v)
    print(max_)
