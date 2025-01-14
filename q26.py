# P.109

import copy


YOKO, TATE = 10, 10


def search(prev: list, depth: int, log: dict, goal: list) -> None:
    target = []
    for parking, w, h in prev:
        for dw, dh in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nw, nh = w + dw, h + dh
            if parking[nw][nh] != 9:
                temp = list(copy.deepcopy(parking))
                temp[w][h], temp[nw][nh] = temp[nw][nh], temp[w][h]
                key = (tuple(map(tuple, temp)), nw, nh)
                if key not in log.keys():
                    target.append([temp, nw, nh])
                    log[key] = depth + 1
    if [goal, YOKO, TATE] in target:
        return
    if len(target) > 0:
        search(prev=target, depth=depth + 1, log=log, goal=goal)


if __name__ == '__main__':
    parking = [[1] * (YOKO + 2) for _ in range(TATE + 2)]
    for w in range(YOKO + 2):
        parking[w][0] = parking[w][TATE + 1] = 9
    for h in range(TATE + 2):
        parking[0][h] = parking[YOKO + 1][h] = 9

    goal = copy.deepcopy(parking)
    goal[1][1] = 2
    goal_key = (tuple(map(tuple, goal)), YOKO, TATE)

    start = copy.deepcopy(parking)
    start[YOKO][TATE] = 2

    log = {}
    start_a = (tuple(map(tuple, start)), YOKO, TATE - 1)
    log[start_a] = 0
    start_b = (tuple(map(tuple, start)), YOKO - 1, TATE)
    log[start_b] = 0
    search(prev=[[start, YOKO, TATE - 1], [start, YOKO - 1, TATE]], depth=0, log=log, goal=goal)
    print(log[goal_key])
