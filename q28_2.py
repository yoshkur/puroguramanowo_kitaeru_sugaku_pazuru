# P.117

from itertools import product

CLUB = [[11000, 40], [8000, 30], [400, 24], [800, 20], [900, 14], [1800, 16], [1000, 15], [7000, 40], [100, 10], [300, 12]]

N = 150


if __name__ == '__main__':
    area = [[0] * (N + 1) for _ in range(len(CLUB) + 1)]
    for i, j in product(range(len(CLUB) - 1, -1, -1), range(N + 1)):
        if j < CLUB[i][1]:
            area[i][j] = area[i + 1][j]
        else:
            area[i][j] = max([
                area[i + 1][j],
                area[i + 1][j - CLUB[i][1]] + CLUB[i][0]
            ])
    print(area[0][N])
