# P.195

from itertools import product


N = 4


def repeated_permutation(iterable, r: int) -> list:
    return product(iterable, repeat=r)


def search(count: dict):
    for rows in repeated_permutation(iterable=range(2 ** N), r=N):
        col_count = [0] * N
        for c in range(N):
            for r in rows:
                if r & (1 << c):
                    col_count[c] += 1
        row_count = [bin(r).count('1') for r in rows]
        key = tuple(row_count + col_count)
        count[key] = count.get(key, 0) + 1


if __name__ == '__main__':
    count = {}
    search(count=count)
    print(len([value for value in count.values() if value == 1]))
