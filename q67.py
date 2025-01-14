# P.293

from itertools import product


W, H = 6, 5


def fill(x: int, y: int, from_: int, to_: int, puzzle: list):
    if puzzle[x][y] == from_:
        puzzle[x][y] = to_
        fill(x=x - 1, y=y, from_=from_, to_=to_, puzzle=puzzle)
        fill(x=x + 1, y=y, from_=from_, to_=to_, puzzle=puzzle)
        fill(x=x, y=y - 1, from_=from_, to_=to_, puzzle=puzzle)
        fill(x=x, y=y + 1, from_=from_, to_=to_, puzzle=puzzle)


def check(puzzle: list) -> bool:
    x, y = 1, 1
    if puzzle[x][y] == 1:
        x += 1
    fill(x=x, y=y, from_=0, to_=2, puzzle=puzzle)
    result = sum(puzzle, []).count(0) == 0
    fill(x=x, y=y, from_=2, to_=0, puzzle=puzzle)
    return result


def search(x: int, y: int, puzzle: list) -> int:
    if x == W + 1:
        x, y = 1, y + 1
    if y == H + 1:
        return 1

    count = search(x=x + 1, y=y, puzzle=puzzle)
    if puzzle[x - 1][y] != 1 and puzzle[x][y - 1] != 1:
        puzzle[x][y] = 1
        if check(puzzle=puzzle):
            count += search(x=x + 1, y=y, puzzle=puzzle)
        puzzle[x][y] = 0

    return count


if __name__ == '__main__':
    puzzle = [[0] * (H + 2) for _ in range(W + 2)]
    for w, h in product(range(W + 2), range(H + 2)):
        if w == 0 or w == W + 1 or h == 0 or h == H + 1:
            puzzle[w][h] = -1

    print(search(x=1, y=1, puzzle=puzzle))
