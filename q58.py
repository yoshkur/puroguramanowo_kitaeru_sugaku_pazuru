# P.243

N = 14


if __name__ == '__main__':
    status = [[N, 0, 0, 0,]]
    step = 0
    while len(list(filter(lambda s: s[1] == N, status))) == 0:
        next_status = []
        for s in status:
            for b in range(s[1] + 1):
                for c in range(s[2] + 1):
                    if s[2] > 0:
                        if s[0] - b - c + 1 >= 0:
                            next_status.append([
                                s[0] - b - c + 1,
                                s[1] + c,
                                s[2] + b - 1,
                                s[3] + 1,
                            ])
                    if s[0] - b - c >= 0:
                        next_status.append([
                            s[0] - b - c,
                            s[1] + c,
                            s[2] + b,
                            s[3],
                        ])
                    if s[0] - b - c - 1 >= 0:
                        next_status.append([
                            s[0] - b - c - 1,
                            s[1] + c + 1,
                            s[2] + b,
                            s[3] + 1
                        ])
        status = list(set(map(tuple, next_status)) - set(map(tuple, status)))
        step += 1

    print(step)
    print(min(list(filter(lambda s: s[1] == N, status)), key=lambda x: x[3]))
