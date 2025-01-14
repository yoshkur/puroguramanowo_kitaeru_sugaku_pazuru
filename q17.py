# P.79

BOY, GIRL = 'B', 'G'
NINZUU = 30


def add(seq: str) -> int:
    if len(seq) == NINZUU:
        return 1

    count = add(seq=seq + BOY)
    if seq[-1] == BOY:
        count += add(seq=seq + GIRL)
    return count


if __name__ == '__main__':
    print(add(seq=BOY) + add(seq=GIRL))
