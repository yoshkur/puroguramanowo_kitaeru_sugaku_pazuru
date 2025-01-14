# P.195

N = 4


def search(rows: list):
    if len(rows) == N:
        return 1

    count = 0
    for row in range(2 ** N):
        cross = [r for r in rows if (row & ~r) > 0 and (~row & r) > 0]
        if not len(cross):
            count += search(rows=rows + [row])
    return count


if __name__ == '__main__':
    print(search(rows=[]))
