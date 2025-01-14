# P.141

from itertools import product

KASO_BOARD_SIZE = 1 + 9 + 1


def search(x: int, y: int, dx: int, dy: int, board: list, check: dict):
    if board[x][y]:
        return
    check[x * 10 + y] = 1
    search(x=x + dx, y=y + dy, dx=dx, dy=dy, board=board, check=check)


if __name__ == '__main__':
    board = [[0] * KASO_BOARD_SIZE for _ in range(KASO_BOARD_SIZE)]
    for index in range(KASO_BOARD_SIZE):
        board[0][index] = True
        board[KASO_BOARD_SIZE - 1][index] = True
        board[index][0] = True
        board[index][KASO_BOARD_SIZE - 1] = True

    count = 0
    for hy, hx, ky, kx in product(range(1, 10), range(1, 10), range(1, 10), range(1, 10),):
        if hx != kx or hy != ky:
            check = {}
            board[hx][hy] = board[kx][ky] = True
            for hd in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                search(x=hx + hd[0], y=hy + hd[1], dx=hd[0], dy=hd[1], board=board, check=check)
            for kd in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                search(x=kx + kd[0], y=ky + kd[1], dx=kd[0], dy=kd[1], board=board, check=check)
            board[hx][hy] = board[kx][ky] = False
            count += len(check)

    print(count)
