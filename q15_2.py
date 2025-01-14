# P.71

from itertools import product


DANSU = 10
MAX_STEPS = 4


def move(a_current: int, b_current: int, memo: dict) -> dict:
    key = (a_current, b_current)
    if key in memo.keys():
        return memo[key]
    if a_current > b_current:
        memo[key] = 0
        return 0
    if a_current == b_current:
        memo[key] = 1
        return 1

    count = 0
    for a_idou_ryou, b_idou_ryou in product(range(1, MAX_STEPS + 1), range(1, MAX_STEPS + 1)):
        count += move(a_current + a_idou_ryou, b_current - b_idou_ryou, memo=memo)
    memo[key] = count
    return count


if __name__ == '__main__':
    memo = {}
    print(move(a_current=0, b_current=DANSU, memo=memo))
