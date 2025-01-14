# P.203

N = 8


if __name__ == '__main__':
    start = (1 << N) - 1
    mask = (1 << N * 2) - 1

    goal1 = 0
    for _ in range(N):
        goal1 = (goal1 << 2) + 1
    goal2 = mask - goal1

    count = N * 2
    for i in range(1 << N * 2):
        turn = i ^ (i << 1) ^ (i << 2)
        turn = (turn ^ (turn >> (N * 2))) & mask

        if start ^ turn == goal1 or start ^ turn == goal2:
            count = min([count, bin(i).count('1')])

    print(count)
