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
        i = 0
        while True:
            card = shuffle(card=card)
            i += 1
            if card == init:
                break
        if i == 2 * (n - 1):
            count += 1

    print(count)
