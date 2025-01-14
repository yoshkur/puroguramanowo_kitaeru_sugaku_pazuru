# P.297

from math import factorial


N = 6

FREE, USED, WALL = 0, 1, 9


def search(person: int, seat: list) -> int:
    count = 0

    for i in range(len(seat)):
        if seat[i] == FREE:
            if seat[i - 1] != USED and seat[i + 1] != USED:
                seat[i] = USED
                count += search(person=person + 1, seat=seat)
                seat[i] = FREE

    return count if count > 0 else factorial(seat.count(FREE))


if __name__ == '__main__':
    seat = [WALL] + [FREE] * N + [WALL] + [FREE] * N + [WALL]

    print(search(0, seat=seat))
