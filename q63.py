# P.273
from datetime import date
from calendar import monthrange
from itertools import product

WEEKS, DAYS = 6, 7


def max_rectangle(cal: list):
    rect = 0
    for sr, sc in product(range(WEEKS), range(DAYS)):
        for er, ec in product(range(sr, WEEKS + 1), range(sc, DAYS + 1)):
            is_weekday = True
            for r, c in product(range(sr, er + 1), range(sc, ec + 1)):
                if c + r * DAYS < WEEKS * DAYS and cal[c + r * DAYS] == 0:
                    is_weekday = False
            if is_weekday:
                rect = max(rect, (er - sr + 1) * (ec - sc + 1))
    return rect


def calc(y: int, m: int, holidays: list):
    cal = [0] * WEEKS * DAYS
    first = wday = date(year=y, month=m, day=1).weekday()
    for d in range(monthrange(year=y, month=m)[1]):
        if 0 <= wday < 5 and (y, m, d + 1) not in holidays:
            cal[first + d] = 1
        wday = (wday + 1) % DAYS
    return max_rectangle(cal=cal)


if __name__ == '__main__':
    holidays = []
    with open(file='sample/q63.txt', mode='r', encoding='utf-8') as fs:
        for line in fs.readlines():
            holidays.append(tuple(map(int, line.split('/'))))

    goukei = 0
    for y, m in product(range(2006, 2016), range(1, 13)):
        goukei += calc(y=y, m=m, holidays=holidays)
    print(goukei)
