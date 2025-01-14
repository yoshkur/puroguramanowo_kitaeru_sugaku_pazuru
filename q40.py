# P.167

from itertools import permutations

N = 9


def solve(cards: list, init: list, depth: int, max_list: list):
    global max_

    if cards[0] == 1:
        if max_ < depth:
            max_ = depth
            max_list.clear()
        if max_ == depth:
            max_list.extend(init)
    else:
        solve(cards=cards[:cards[0]][::-1] + cards[cards[0]: N], init=init, depth=depth + 1, max_list=max_list)


if __name__ == '__main__':
    max_ = 0
    max_list = []
    for suuretsu in permutations(range(1, N + 1)):
        solve(cards=suuretsu, init=suuretsu, depth=0, max_list=max_list)
    print(max_)
    print(max_list)
