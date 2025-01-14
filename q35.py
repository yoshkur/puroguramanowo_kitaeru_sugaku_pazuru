# P.145

N = 6


def search(man_x: int, man_y: int, woman_x: int, woman_y: int, meet: int):
    global count

    if not (man_x <= N and man_y <= N and woman_x >= 0 and woman_y >= 0):
        return

    count += 1 if man_x == N and man_y == N and meet >= 2 else 0
    meet += 1 if man_x == woman_x else 0
    meet += 1 if man_y == woman_y else 0
    search(man_x=man_x + 1, man_y=man_y, woman_x=woman_x - 1, woman_y=woman_y, meet=meet)
    search(man_x=man_x + 1, man_y=man_y, woman_x=woman_x, woman_y=woman_y - 1, meet=meet)
    search(man_x=man_x, man_y=man_y + 1, woman_x=woman_x - 1, woman_y=woman_y, meet=meet)
    search(man_x=man_x, man_y=man_y + 1, woman_x=woman_x, woman_y=woman_y - 1, meet=meet)


if __name__ == '__main__':
    count = 0
    search(man_x=0, man_y=0, woman_x=N, woman_y=N, meet=0)
    print(count)
