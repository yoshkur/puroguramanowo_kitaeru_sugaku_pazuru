# P.183

from copy import deepcopy
from itertools import permutations
from math import gcd


def search(abc, depth, max_abc, log):
    key = tuple(abc)
    if key in log:
        return False
    if abc[0] == max_abc[0] / 2:
        return True
    log[key] = depth
    for i, j in permutations(range(3), 2):
        if abc[i] > 0 or abc[j] < max_abc[j]:
            next_abc = deepcopy(abc)
            move = min(abc[i], max_abc[j] - abc[j])
            next_abc[i] -= move
            next_abc[j] += move
            if search(abc=next_abc, depth=depth + 1, max_abc=max_abc, log=log):
                return True
    return False


if __name__ == '__main__':
    count = 0
    for a in range(10, 101, 2):
        for c in range(1, a // 2):
            b = a - c
            if gcd(b, c) == 1:
                count += 1 if search(abc=[a, 0, 0], depth=0, max_abc=[a, b, c], log={}) else 0
    print(count)
