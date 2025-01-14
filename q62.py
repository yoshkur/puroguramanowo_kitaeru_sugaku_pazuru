# P.267

W, H = 5, 4


def search(x: int, y: int, depth: int, move: list, map_: list):
    if x < 0 or W <= x or y < 0 or H <= y or map_[x + y * W]:
        return 0
    if depth == W * H:
        return 1

    count = 0

    map_[x + y * W] = True
    for m in move:
        count += search(x=x + m[0], y=y + m[1], depth=depth + 1, move=move, map_=map_)
    map_[x + y * W] = False
    return count


if __name__ == '__main__':
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    map_ = [False] * W * H

    count = 0
    for i in range(W * H):
        count += search(x=i % W, y=i // W, depth=1, move=move, map_=map_)

    print(count // 2)
