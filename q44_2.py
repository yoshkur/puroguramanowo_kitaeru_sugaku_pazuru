# P.183

from math import gcd


if __name__ == '__main__':
    count = 0
    for a in range(10, 101, 2):
        for c in range(1, a // 2):
            b = a - c
            if gcd(b, c) == 1:
                count += 1
    print(count)
