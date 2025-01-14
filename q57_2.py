# P.237

def make_bars(v: int, h: list):
    global V
    global H

    new_h = [0] * (len(h) + v - 1)
    for i in range(v):
        for j, count in enumerate(h):
            new_h[i + j] += count
    if v == V + 1:
        print(h[H])
    else:
        make_bars(v=v + 1, h=new_h)


if __name__ == '__main__':
    V, H = 7, 10

    make_bars(v=1, h=[1])
