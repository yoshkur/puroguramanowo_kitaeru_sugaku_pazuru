# P.191

from copy import deepcopy
from itertools import combinations


N = 7


if __name__ == '__main__':
    checked = {tuple(range(1, N + 1)): 0}
    check = [list(range(1, N + 1))]
    depth = 0

    while len(check):
        next_check = []
        for i, j in combinations(range(N), 2):
            for c in check:
                d = deepcopy(c)
                d[i], d[j] = d[j], d[i]
                key = tuple(d)
                if key not in checked.keys():
                    checked[key] = depth + 1
                    next_check.append(d)
        check = next_check
        depth += 1

    print(sum(checked.values()))
