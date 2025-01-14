# P.211

from copy import deepcopy


def shuffle(card: list):
    left = card[:len(card) // 2]
    right = card[len(card) // 2:]
    result = []
    for i in range(len(left)):
        result.append(left[i])
        result.append(right[i])
    return result


if __name__ == '__main__':
    count = 0
    for n in range(1, 101):
        init = list(range(1, 2 * n + 1))
        card = deepcopy(init)
        for i in range(2 * (n - 1)):
            card = shuffle(card=card)
        if card == init:
            count += 1

    print(count)
