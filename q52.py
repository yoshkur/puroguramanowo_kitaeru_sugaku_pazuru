# P.215

from itertools import permutations

N = 8


if __name__ == '__main__':
    goal = [1] * N

    count = 0
    for init in permutations(range(1, N + 1)):
        hour_glass = init
        pos = 0
        log = {}

        key = tuple(hour_glass)
        while log.get(key) != pos:
            if hour_glass == goal:
                count += 1
                break
            log[key] = pos

            hour_glass = [h - 1 if h > 0 else 0 for h in hour_glass]
            for i in range(init[pos]):
                rev = (pos + i) % N
                hour_glass[rev] = init[rev] - hour_glass[rev]

            pos = (pos + 1) % N
            key = tuple(hour_glass)

    print(count)
