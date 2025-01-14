# P.179
# すごく時間が掛かるが答えは出る。

N = 5

if __name__ == '__main__':
    cards = [list(range(1, 2 * N + 1))]
    answer = list(range(1, 2 * N + 1))[::-1]

    depth = 1
    while True:
        cards = [
            result for c in cards for result in [
                c[i: i + N] + c[0: i] + c[i + N:]
                for i in range(1, N + 1)
            ]
        ]

        if answer in cards:
            break
        depth += 1

    print(depth)
