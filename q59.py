# P.247

from copy import deepcopy
from collections import deque

N = 8


def search(child: list, oni: int, oni_pos: int, step: int, log: str, goal: list):
    global min_step

    if oni == 0:
        if child in goal:
            print(f'#{step} #{log}')
            min_step = min(step, min_step)
            return

    for i in range(1, N):
        if step + N + i <= min_step:
            next_child = deepcopy(child)
            pos = (oni_pos + i) % N
            next_child[pos] = oni
            next_oni = child[pos]
            search(child=next_child, oni=next_oni, oni_pos=pos, step=step + N + i, log=log + str(pos), goal=goal)


if __name__ == '__main__':
    min_step = 98
    goal = []
    base_list = list(range(1, N + 1))[::-1]
    for i in range(1, N + 1):
        x = deque(base_list)
        x.rotate(i)
        goal.append(list(x))

    search(child=[0] + list(range(2, N + 1)), oni=1, oni_pos=0, step=N, log='0', goal=goal)
