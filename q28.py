# P.117

from itertools import combinations


CLUB = [[11000, 40], [8000, 30], [400, 24], [800, 20], [900, 14], [1800, 16], [1000, 15], [7000, 40], [100, 10], [300, 12]]

N = 150


if __name__ == '__main__':
    max_ = 0
    for i in range(1, len(CLUB) + 1):
        for array in combinations(CLUB, i):
            if sum(map(lambda x: x[1], array)) <= N:
                max_ = max(max_, sum(map(lambda x: x[0], array)))
    print(max_)
