# P.131

SQUARE = 6


def route(x: int, y: int, is_first_time: bool, is_used: list):
    global count

    if x == SQUARE and y == SQUARE:
        if is_first_time:
            route(x=0, y=0, is_first_time=False, is_used=is_used)
        else:
            count += 1

    if x < SQUARE:
        if not is_used[x][y][0]:
            is_used[x][y][0] = True
            route(x=x + 1, y=y, is_first_time=is_first_time, is_used=is_used)
            is_used[x][y][0] = False
    if y < SQUARE:
        if not is_used[x][y][1]:
            is_used[x][y][1] = True
            route(x=x, y=y + 1, is_first_time=is_first_time, is_used=is_used)
            is_used[x][y][1] = False


if __name__ == '__main__':
    count = 0
    is_used = []
    for _ in range(SQUARE + 1):
        temp_list = []
        for _ in range(SQUARE + 1):
            temp_list.append([False, False])
        is_used.append(temp_list)
    route(x=0, y=0, is_first_time=True, is_used=is_used)
    print(count)
