# P.41


IDO_KAISU = 12
IDO = [
    {'tate': 0, 'yoko': 1},
    {'tate': 0, 'yoko': -1},
    {'tate': 1, 'yoko': 0},
    {'tate': -1, 'yoko': 0},
]


def move(log: list) -> int:
    if len(log) == IDO_KAISU + 1:
        return 1

    count = 0
    for ido_ in IDO:
        current_position = log[-1]
        next_position = {'tate': current_position.get('tate') + ido_.get('tate'), 'yoko': current_position.get('yoko') + ido_.get('yoko')}
        if next_position not in log:
            count += move(log=log + [next_position])
    return count


if __name__ == '__main__':
    print(move(log=[{'tate': 0, 'yoko': 0}]))
