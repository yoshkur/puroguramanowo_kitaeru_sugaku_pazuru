# P.121
# 正しく動作していない。

from itertools import product, combinations
from fractions import Fraction


def calculate_product(array):
    result = array[0]
    for index in range(1, len(array)):
        result = product(result, array[index])
    return [list(item) for item in result]


def parallel(array: list) -> Fraction:
    return Fraction(1, sum(list(map(lambda i: Fraction(1, i), array))))


def calc(n: int) -> list:
    global memo

    if n in memo.keys():
        return memo[n]

    # result = [i + 1 for i in calc(n=n - 1)]
    result = list(map(lambda i: i + 1, calc(n=n - 1)))

    for i in range(2, n + 1):
        cut = {}
        for array in combinations(range(1, n), i - 1):
            pos = 0
            r = []
            for j in range(len(array)):
                r.append(array[j] - pos)
                pos = array[j]
            r.append(n - pos)
            # cut[tuple(sorted(r))] = 1
            key = tuple(sorted(r))
            cut[key] = 1
        keys = [calc(n=e) for c in cut.keys() for e in c]
        product_keys = list(map(product, keys))
        for k in product_keys:
            for vv in k:
                result.append(parallel(array=vv))
        # product_keys = list(map(calculate_product, keys))
        # for k in product_keys:
        #     for vv in k:
        #         result.append(parallel(array=vv))
    memo[n] = result
    return result


if __name__ == '__main__':
    memo = {1: [1]}
    golden_ratio = 1.61800339887
    min_ = float('inf')
    for i in calc(n=10):
        if abs(golden_ratio - i) < abs(golden_ratio - min_):
            min_ = i
    print(f'{min_:.10f}')
    print(min_)
