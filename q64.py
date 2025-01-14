# P.277
from itertools import product


N = 5
DX = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def search(maze: list, p1: list, d1: int, p2: list, d2: int):
    if len(p1) == len(p2):
        if p1[-1][:2] == p2[-1][:2]:
            return True
        if p1[-1][:2] == [N - 1, N - 1]:
            return False
        if p2[-1][:2] == [0, 0]:
            return False
    if p1.count(p1[-1]) > 1:
        return False

    pre = p1[-1]
    for i in range(len(DX)):
        d = (d1 - 1 + i) % len(DX)
        px = pre[0] + DX[d][0]
        py = pre[1] + DX[d][1]
        if 0 <= px < N and 0 <= py < N and maze[px + N * py] == 0:
            return search(maze=maze, p1=p2, d1=d2, p2=p1 + [[px, py, d]], d2=d)

    return False


if __name__ == '__main__':
    a = [[0, 0, -1]]
    b = [[N - 1, N - 1, -1]]
    count = 0
    for maze in product([0, 1], repeat=N ** 2 - 2):
        if search(maze=[0] + list(maze) + [0], p1=a, d1=3, p2=b, d2=1):
            count += 1

    print(count)
