# P.41


IDO_KAISU = 12
IDO = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def move(log):
    if len(log) == IDO_KAISU + 1:
        return 1

    count = 0
    for ido_ in IDO:
        next_position = [log[-1][0] + ido_[0], log[-1][1] + ido_[1]]
        if next_position not in log:
            count += move(log=log + [next_position])
    return count


if __name__ == '__main__':
    print(move(log=[[0, 0]]))
