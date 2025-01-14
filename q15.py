# P.71

from itertools import product


DANSU = 10
MAX_STEPS = 4


def move(a_current: int, b_current: int) -> int:
    if a_current > b_current:
        return 0
    if a_current == b_current:
        return 1

    count = 0
    for a_idou_ryou, b_idou_ryou in product(range(1, MAX_STEPS + 1), range(1, MAX_STEPS + 1)):
        count += move(a_current + a_idou_ryou, b_current - b_idou_ryou)
    return count


if __name__ == '__main__':
    print(move(a_current=0, b_current=DANSU))
