# P.227

from itertools import permutations


def move(base: int, add: int) -> int:
    a0 = (base + add) // 50
    a1 = (base + add) % 50
    b0 = base // 50
    b1 = base % 50

    a2 = a1 // 10
    a3 = a1 % 10
    b2 = b1 // 10
    b3 = b1 % 10

    a4 = a3 // 5
    a5 = a3 % 5
    b4 = b3 // 5
    b5 = b3 % 5

    return abs(a0 - b0) + abs(a2 - b2) + abs(a4 - b4) + abs(a5 - b5)


def count(list_: list) -> int:
    count_value = total = 0
    for i in list_:
        count_value += move(base=total, add=i)
        total += i
    return count_value


if __name__ == '__main__':
    min_ = 100
    for s in permutations(range(1, 11)):
        min_ = min(min_, count(list_=s))
    print(min_)
