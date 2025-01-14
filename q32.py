# P.135

HEIGHT = 4
WIDTH = 7
# HEIGHT = 5
# WIDTH = 6


def print_tatami():
    global str_

    for i in range(1, HEIGHT + 1):
        for j in range(1, WIDTH + 1):
            if tatami[i][j] == tatami[i][j + 1] or tatami[i][j] == tatami[i][j - 1]:
                str_ += '-'
            if tatami[i][j] == tatami[i + 1][j] or tatami[i][j] == tatami[i - 1][j]:
                str_ += '|'
        str_ += '\n'
    str_ += '\n'


def set_tatami(h: int, w: int, id: int, tatami: list):
    if h == HEIGHT + 1:
        print_tatami()
    elif w == WIDTH + 1:
        set_tatami(h=h + 1, w=1, id=id, tatami=tatami)
    elif tatami[h][w] > 0:
        set_tatami(h=h, w=w + 1, id=id, tatami=tatami)
    else:
        if tatami[h - 1][w - 1] == tatami[h - 1][w] or tatami[h - 1][w - 1] == tatami[h][w - 1]:
            if tatami[h][w + 1] == 0:
                tatami[h][w] = tatami[h][w + 1] = id
                set_tatami(h=h, w=w + 2, id=id + 1, tatami=tatami)
                tatami[h][w] = tatami[h][w + 1] = 0
            if tatami[h + 1][w] == 0:
                tatami[h][w] = tatami[h + 1][w] = id
                set_tatami(h=h, w=w + 1, id=id + 1, tatami=tatami)
                tatami[h][w] = tatami[h + 1][w] = 0


if __name__ == '__main__':
    str_ = ''
    tatami = [[0] * (WIDTH + 2) for _ in range(HEIGHT + 2)]
    for h in range(HEIGHT + 2):
        tatami[h][0] = -1
        tatami[h][WIDTH + 1] = -1
    for w in range(WIDTH + 2):
        tatami[0][w] = -1
        tatami[HEIGHT + 1][w] = -1
    set_tatami(h=1, w=1, id=1, tatami=tatami)
    print(str_)
