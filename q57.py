# P.237

from itertools import permutations, takewhile


if __name__ == '__main__':
    v, h = 7, 10
    total = 0
    for final in permutations(range(v)):
        count = 0
        for i in range(v):
            response_list = list(filter(lambda k: k > i, takewhile(lambda j: j != i, final)))
            count += len(response_list)
        if count == h:
            total += 1

    print(total)
