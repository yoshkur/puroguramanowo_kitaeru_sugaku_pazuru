# P.83
import math


def check(kiriwake_suu: int, pre: int, log: list, square: list):
    if kiriwake_suu == len(log):
        if 1 + pre in square:
            print(kiriwake_suu)
            print(log)
            return True
    else:
        list_ = list(set(range(1, kiriwake_suu + 1)) - set(log))
        for index in list_:
            if pre + index in square:
                if check(kiriwake_suu=kiriwake_suu, pre=index, log=log + [index], square=square):
                    return True
    return False


if __name__ == '__main__':
    kiriwake_suu = 2
    while True:
        square = [i ** 2 for i in range(2, math.floor(math.sqrt(kiriwake_suu * 2)) + 1)]
        if check(kiriwake_suu=kiriwake_suu, pre=1, log=[1], square=square):
            break
        kiriwake_suu += 1
